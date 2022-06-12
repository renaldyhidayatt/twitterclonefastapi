"""Create Comment

Revision ID: 8bfa325b4830
Revises: f3097c76e58c
Create Date: 2022-06-13 06:23:54.001231

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8bfa325b4830'
down_revision = 'f3097c76e58c'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('comment',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('commentOn', sa.Integer(), sa.ForeignKey('tweet.id'), nullable=False),
        sa.Column('commentBy', sa.Integer(), sa.ForeignKey('user.id'), nullable=False),
        sa.Column('comment', sa.String(length=255), nullable=False),
        sa.Column('commentAt', sa.DateTime(timezone=True), default=sa.func.now()),
    )


def downgrade() -> None:
    op.drop_table('comment')
