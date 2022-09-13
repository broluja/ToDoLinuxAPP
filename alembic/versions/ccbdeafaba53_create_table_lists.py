"""
Create table "lists"

Revision ID: ccbdeafaba53
Revises: 
Create Date: 2022-08-14 09:18:35.762070

"""
from alembic import op
import sqlalchemy as sa

from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'ccbdeafaba53'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'lists',
        sa.Column('id', postgresql.UUID(), primary_key=True),
        sa.Column('name', sa.String())
    )


def downgrade() -> None:
    op.drop_table('lists')
