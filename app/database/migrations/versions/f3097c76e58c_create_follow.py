"""Create Follow

Revision ID: f3097c76e58c
Revises: 930163af7e6e
Create Date: 2022-06-13 06:23:07.405392

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f3097c76e58c'
down_revision = '930163af7e6e'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('follow',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column("sender", sa.Integer(), sa.ForeignKey('user.id'), nullable=False),
        sa.Column("receiver", sa.Integer(), sa.ForeignKey('user.id'), nullable=False),
        sa.Column('followOn', sa.DateTime(timezone=True), default=sa.func.now()),
    )


def downgrade() -> None:
    op.drop_table('follow')
