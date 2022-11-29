"""Create Users

Revision ID: 94c48d863634
Revises: 
Create Date: 2022-06-13 06:16:03.260485

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '94c48d863634'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('users',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('firstName', sa.String(length=255), nullable=False),
        sa.Column('lastName', sa.String(length=255), nullable=False),

        sa.Column('username', sa.String(length=255), nullable=False),
        sa.Column('email', sa.String(length=255), nullable=False, unique=True),
        sa.Column('password', sa.String(length=255), nullable=False),
        sa.Column('profileImage', sa.String(length=255), nullable=True, default="defaultProfilePic.png"),
        sa.Column('profileCover', sa.String(length=255), nullable=True, default="backgroundCoverPic.svg"),
        sa.Column('bio', sa.String(length=255), nullable=True),
        sa.Column('country', sa.String(length=255), nullable=True),
        sa.Column('website', sa.String(length=255), nullable=True),
    )


def downgrade() -> None:
    op.drop_table('users')
