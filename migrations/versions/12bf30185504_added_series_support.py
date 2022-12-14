"""Added series support

Revision ID: 12bf30185504
Revises: a141dc7c6f98
Create Date: 2022-03-21 23:34:24.557158

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '12bf30185504'
down_revision = 'a141dc7c6f98'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('saved_series',
    sa.Column('id', sa.String(length=100), nullable=False),
    sa.Column('imdb_id', sa.String(length=100), nullable=False),
    sa.Column('keywords', sa.String(length=100), nullable=False),
    sa.Column('tmdb_data', sa.Text(), nullable=False),
    sa.Column('omdb_data', sa.Text(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id'),
    sa.UniqueConstraint('imdb_id')
    )
    op.create_table('series',
    sa.Column('id', sa.String(length=100), nullable=False),
    sa.Column('imdb_id', sa.String(length=100), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('original_name', sa.Text(), nullable=False),
    sa.Column('release_year', sa.String(length=100), nullable=False),
    sa.Column('posterLink', sa.Text(), nullable=False),
    sa.Column('no_of_episodes', sa.String(length=100), nullable=False),
    sa.Column('directLinks', sa.Text(), nullable=False),
    sa.Column('genre', sa.String(length=100), nullable=False),
    sa.Column('language', sa.String(length=100), nullable=False),
    sa.Column('imdb_rating', sa.String(length=100), nullable=False),
    sa.Column('runtime', sa.String(length=100), nullable=False),
    sa.Column('is_adult', sa.Boolean(), nullable=False),
    sa.Column('is_archived', sa.Boolean(), nullable=False),
    sa.Column('watch_count', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('directLinks'),
    sa.UniqueConstraint('id'),
    sa.UniqueConstraint('imdb_id'),
    sa.UniqueConstraint('posterLink')
    )
    op.create_table('series_request',
    sa.Column('id', sa.String(length=100), nullable=False),
    sa.Column('imdb_URL', sa.String(length=100), nullable=False),
    sa.Column('posterLink', sa.String(length=100), nullable=False),
    sa.Column('requestor', sa.String(length=100), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('original_name', sa.String(length=100), nullable=True),
    sa.Column('release_year', sa.String(length=100), nullable=False),
    sa.Column('isfulfilled', sa.Boolean(), nullable=False),
    sa.Column('status', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id'),
    sa.UniqueConstraint('imdb_URL'),
    sa.UniqueConstraint('posterLink')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('series_request')
    op.drop_table('series')
    op.drop_table('saved_series')
    # ### end Alembic commands ###
