"""Create Messages

Revision ID: 4bc714dc2983
Revises: 227a3f11c23b
Create Date: 2022-06-13 06:21:11.415639

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4bc714dc2983'
down_revision = '227a3f11c23b'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('messages',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('message', sa.String(length=255), nullable=False),
        sa.Column('messageTo', sa.Integer(), sa.ForeignKey('user.id'), nullable=False),
        sa.Column('messageFrom', sa.Integer(), sa.ForeignKey('user.id'), nullable=False),
        sa.Column('messageOn', sa.DateTime(timezone=True), default=sa.func.now()),
    )


def downgrade() -> None:
    op.drop_table('messages')
