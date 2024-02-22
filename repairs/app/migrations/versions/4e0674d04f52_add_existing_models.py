"""Add existing models

Revision ID: 4e0674d04f52
Revises: 
Create Date: 2024-02-19 17:11:24.797152

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4e0674d04f52'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('repair_status',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=7), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('repairs',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('car_id', sa.Integer(), nullable=False),
    sa.Column('repair_status', sa.Integer(), nullable=False),
    sa.Column('repair_description', sa.String(length=500), nullable=False),
    sa.Column('start_date', sa.Date()),
    sa.Column('approximate_duration', sa.Integer()),
    sa.Column('garage_name', sa.String(length=100), nullable=False),
    sa.Column('garage_phone', sa.String(length=13), nullable=False),
    sa.ForeignKeyConstraint(['repair_status'], ['repair_status.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('repairs')
    op.drop_table('repair_status')
    # ### end Alembic commands ###
