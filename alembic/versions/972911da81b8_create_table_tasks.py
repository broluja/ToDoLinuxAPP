"""Create table "tasks"

Revision ID: 972911da81b8
Revises: ccbdeafaba53
Create Date: 2022-08-14 18:31:02.478106

"""
from alembic import op
import sqlalchemy as sa

from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '972911da81b8'
down_revision = 'ccbdeafaba53'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'tasks',
        sa.Column('id', postgresql.UUID(), primary_key=True),
        sa.Column('list_id', postgresql.UUID(), sa.ForeignKey('lists.id')),
        sa.Column('title', sa.String()),
        sa.Column('content', sa.String(), nullable=True),
        sa.Column('date', sa.DateTime(timezone=True), nullable=True),
        sa.Column('priority', sa.Enum('LOW', 'MEDIUM', 'HIGH', name='priority_types')),
        sa.Column('is_complete', sa.Boolean(), nullable=True)
    )


def downgrade() -> None:
    op.drop_table('tasks')
