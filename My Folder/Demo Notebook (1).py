# Databricks notebook source
print ('Hello World!')

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT "Hello world from SQL"

# COMMAND ----------

# MAGIC %md
# MAGIC  
# MAGIC # title 1
# MAGIC ## title 2
# MAGIC
# MAGIC

# COMMAND ----------

# MAGIC %run ./Includes/Setup

# COMMAND ----------

print(full_name)

# COMMAND ----------

# MAGIC %fs ls '/databricks-datasets'

# COMMAND ----------

dbutils.help()

# COMMAND ----------


