# Example curl to test QA endpoint
curl -X POST "http://127.0.0.1:8000/qa" -H "Content-Type: application/json" -d '{"question":"What does the MRI show?","k":2}'