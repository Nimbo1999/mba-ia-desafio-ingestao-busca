.PHONY: ingest chat

ingest:
	@python src/ingest.py

chat:
	@python src/chat.py
