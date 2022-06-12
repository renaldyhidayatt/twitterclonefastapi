"""Create Likes

Revision ID: 930163af7e6e
Revises: 4bc714dc2983
Create Date: 2022-06-13 06:22:08.427598

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '930163af7e6e'
down_revision = '4bc714dc2983'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('likes',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('likeOn', sa.Integer(), sa.ForeignKey('user.id'), nullable=False),
        sa.Column('likeBy', sa.Integer(), sa.ForeignKey('tweet.id'), nullable=False),
    )


def downgrade() -> None:
    op.drop_table('likes')
