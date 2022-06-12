"""Create Tweet

Revision ID: 19c431c8ad02
Revises: 94c48d863634
Create Date: 2022-06-13 06:18:03.881057

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '19c431c8ad02'
down_revision = '94c48d863634'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('tweet',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('status', sa.String(length=255), nullable=False),
        sa.Column('tweetBy', sa.Integer(), sa.ForeignKey('user.id'), nullable=False),
        sa.Column('postedOn', sa.DateTime(timezone=True), default=sa.func.now()),
    )


def downgrade() -> None:
    op.drop_table('tweet')
