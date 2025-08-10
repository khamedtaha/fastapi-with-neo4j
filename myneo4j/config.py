from neo4j import GraphDatabase
from dotenv import load_dotenv
import os


load_dotenv()

uri = os.getenv("NEO4J_URI")
username = os.getenv("NEO4J_USERNAME", "neo4j")
password = os.getenv("NEO4J_PASSWORD")


driver = GraphDatabase.driver(uri, auth=(username, password))