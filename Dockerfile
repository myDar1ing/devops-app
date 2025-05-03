FROM python:3-alpine

WORKDIR /code
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
CMD ["hypercorn", "app.main:app", "--bind", "::"]