
# Summary of `lang-01.py`

This script connects to a SQLite database (`worldevents.db`) and retrieves records from the `world_events` table. Each row is transformed into a `Document` object from LangChain, with `page_content` containing the event name and impact, and metadata containing the event type and place name. Finally, it prints the list of `Document` objects, which can later be used in vector stores like Chroma for semantic search or LLM applications.

---

## 🔹 5 Improvements

1. **Use context managers for database connection**  
   Replace manual `connect`/`cursor` handling with Python’s `with` statement to ensure connections are properly closed.

2. **Parameterize SQL queries**  
   Although this query is static, it’s good practice to use parameterized queries to prevent SQL injection when filters are added later.

3. **Improve metadata keys**  
   Remove extra quotes and spaces from metadata keys (`' "Type of Event"' → 'Type of Event'`) for consistency and easier access.

4. **Exception handling**  
   Add try/except blocks for database connection and query execution to handle missing tables or corrupted DB gracefully.

5. **Output formatting**  
   Instead of printing raw `Document` objects, format the output (pretty print JSON, Pandas DataFrame, etc.) for readability.

---

## 🔹 3 Better Alternatives

1. **Use Pandas for data retrieval**  
   ```python
   import pandas as pd
   
   df = pd.read_sql("SELECT [Name of Incident],[Type of Event], Impact,[Place Name] FROM world_events", conn)
   print(df.head())


Direct integration with LangChain loaders
Create a custom LangChain document loader that directly queries SQLite, avoiding manual looping.

Use SQLAlchemy ORM
Define a model for world_events and query with SQLAlchemy for cleaner, more maintainable, and database-agnostic code.


Do you also want me to **add a sample refactored version** of this script (with context managers + Pandas + LangChain integration) so the README looks more developer-friendly?





