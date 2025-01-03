"""Add customization fields to story model

Revision ID: 7a909b6ef7af
Revises: c12af9202d0d
Create Date: 2024-11-11 11:52:59.731904

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7a909b6ef7af'
down_revision: Union[str, None] = 'c12af9202d0d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('stories', sa.Column('summary', sa.String(), nullable=True))
    op.add_column('stories', sa.Column('target_audience', sa.String(), nullable=True))
    op.add_column('stories', sa.Column('theme', sa.String(), nullable=True))
    op.add_column('stories', sa.Column('main_characters', sa.JSON(), nullable=True))
    op.add_column('stories', sa.Column('moral', sa.String(), nullable=True))
    op.add_column('stories', sa.Column('setting', sa.String(), nullable=True))
    op.add_column('stories', sa.Column('story_length', sa.String(), nullable=True))
    op.add_column('stories', sa.Column('genre', sa.String(), nullable=True))
    op.add_column('stories', sa.Column('is_public', sa.Boolean(), nullable=True))
    op.alter_column('stories', 'content',
               existing_type=sa.VARCHAR(),
               type_=sa.Text(),
               existing_nullable=False)
    op.alter_column('stories', 'author_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.drop_index('ix_stories_title', table_name='stories')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index('ix_stories_title', 'stories', ['title'], unique=False)
    op.alter_column('stories', 'author_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('stories', 'content',
               existing_type=sa.Text(),
               type_=sa.VARCHAR(),
               existing_nullable=False)
    op.drop_column('stories', 'is_public')
    op.drop_column('stories', 'genre')
    op.drop_column('stories', 'story_length')
    op.drop_column('stories', 'setting')
    op.drop_column('stories', 'moral')
    op.drop_column('stories', 'main_characters')
    op.drop_column('stories', 'theme')
    op.drop_column('stories', 'target_audience')
    op.drop_column('stories', 'summary')
    # ### end Alembic commands ###
