#!/bin/bash
echo -en "⏳ waiting for PostgreSQL ..."

while ! nc -z "$THIERRY_DB_HOST" "$THIERRY_DB_PORT"; do
  echo -en ".";
  sleep 1;
done

echo -e "\n🚀 PostgreSQL started !"

echo -e "📦 making migrations"
poetry run python manage.py makemigrations || { echo "❌ Makemigrations failed !"; exit 1; }

echo -e "📦 applying migrations"
poetry run python manage.py migrate || { echo "❌ Migration failed !"; exit 1; }

echo -e "🔒 creating super user"
cat << EOF | poetry run python manage.py shell || { echo "❌ Super user creation failed"; exit 1; }
from django.contrib.auth import get_user_model

User = get_user_model()  # get the currently active user model,

User.objects.filter(username='admin').exists() or \
    User.objects.create_superuser('admin', 'admin@admin.admin', 'admin')
EOF

echo "✅ everything's done !"

echo "🧪 running tests"
poetry run pytest
