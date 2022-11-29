"""Create Trends

Revision ID: dab0e7567756
Revises: 19c431c8ad02
Create Date: 2022-06-13 06:19:17.899565

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dab0e7567756'
down_revision = '19c431c8ad02'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('trends',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('hashtag', sa.String(length=255), nullable=False),
        sa.Column('user_id', sa.Integer(), sa.ForeignKey('user.id'), nullable=False),
        sa.Column('tweet_id', sa.Integer(), sa.ForeignKey('tweet.id'), nullable=False),
    )


def downgrade() -> None:
    op.drop_table('trends')
