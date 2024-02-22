"""Add initial repair statuses

Revision ID: 3b0febbc3235
Revises: 4e0674d04f52
Create Date: 2024-02-19 17:12:54.107142

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3b0febbc3235'
down_revision = '4e0674d04f52'
branch_labels = None
depends_on = None


def upgrade():
    op.execute("INSERT INTO repair_status (name) VALUES ('started'), ('pending'),('ready');")


def downgrade():
    op.execute('DELETE FROM repair_status')
