"""Create Retweet

Revision ID: 227a3f11c23b
Revises: dab0e7567756
Create Date: 2022-06-13 06:20:07.790475

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '227a3f11c23b'
down_revision = 'dab0e7567756'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('retweet',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('retweetBy', sa.Integer(), sa.ForeignKey('user.id'), nullable=False),
        sa.Column('retweetFrom', sa.Integer(), sa.ForeignKey('tweet.id'), nullable=False),
        sa.Column("status", sa.String(length=255), nullable=False),
        sa.Column('tweetOn', sa.DateTime(timezone=True), default=sa.func.now()),
    )


def downgrade() -> None:
    op.drop_table('retweet')
