

def create_profile(tx, name, age, email):
   tx.run("""
      MERGE (p:Profile {email: $email})
      ON CREATE SET p.name = $name, p.age = $age
      
      MERGE (d:Doctor {email: $email})
      ON CREATE SET d.name = $name
      
      MERGE (p)-[:REGISTERED_WITH]->(d)
   """, name=name, age=age, email=email)


def read_profiles(tx):
   query = "MATCH (p:Profile) RETURN p.name AS name, p.age AS age, p.email AS email"
   result = tx.run(query)
   return [{"name": record["name"], "age": record["age"], "email": record["email"]} for record in result]



def add_specialization(tx, email, specialization):
   query = """
      MATCH (d:Doctor {email: $email})
      MERGE (s:Specialization {name: $specialization})
      MERGE (d)-[:SPECIALIZED_IN]->(s)
   """
   tx.run(query, email=email, specialization=specialization)



def new_specialization(tx, specialization):
   query = """
      CREATE (s:Specialization {name: $specialization})
   """
   tx.run(query, specialization=specialization)
