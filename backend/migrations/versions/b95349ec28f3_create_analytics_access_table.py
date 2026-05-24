"""create analytics_access table

Revision ID: b95349ec28f3
Revises: 383a9988902a
Create Date: 2026-05-24 15:52:18.743234

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

revision: str = 'b95349ec28f3'
down_revision: Union[str, Sequence[str], None] = '383a9988902a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'analytics_access',

        sa.Column('id', sa.UUID(), nullable=False),

        sa.Column('route', sa.String(length=255), nullable=False),

        sa.Column('timestamp', sa.DateTime(), nullable=False),

        sa.Column('user_agent', sa.String(length=500), nullable=False),

        sa.Column('language', sa.String(length=50), nullable=False),

        sa.Column('platform', sa.String(length=100), nullable=False),

        sa.Column('screen_width', sa.Integer(), nullable=False),

        sa.Column('screen_height', sa.Integer(), nullable=False),

        sa.Column('timezone', sa.String(length=100), nullable=False),

        sa.Column('sessionId', sa.String(length=255), nullable=False),

        sa.Column('fingerprint', sa.String(length=255), nullable=False),

        sa.Column('ip_address', sa.String(length=100), nullable=False),

        sa.Column('country', sa.String(length=100), nullable=False),

        sa.Column('bot_detection', sa.Boolean(), nullable=False),

        sa.Column('authenticate_user_id', sa.String(length=255), nullable=True),

        sa.PrimaryKeyConstraint('id')
    )

    op.create_index(
        op.f('ix_analytics_access_sessionId'),
        'analytics_access',
        ['sessionId'],
        unique=False
    )

    op.create_index(
        op.f('ix_analytics_access_fingerprint'),
        'analytics_access',
        ['fingerprint'],
        unique=False
    )

    op.create_index(
        op.f('ix_analytics_access_ip_address'),
        'analytics_access',
        ['ip_address'],
        unique=False
    )


def downgrade() -> None:
    op.drop_index(
        op.f('ix_analytics_access_ip_address'),
        table_name='analytics_access'
    )

    op.drop_index(
        op.f('ix_analytics_access_fingerprint'),
        table_name='analytics_access'
    )

    op.drop_index(
        op.f('ix_analytics_access_sessionId'),
        table_name='analytics_access'
    )

    op.drop_table('analytics_access')
