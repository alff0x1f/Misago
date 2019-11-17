"""cache_versions

Revision ID: e312cfb04cf7
Revises: 
Create Date: 2019-11-02 15:16:47.164010

"""
from alembic import op
import sqlalchemy as sa
from misago.cacheversions.utils import generate_version_string


# revision identifiers, used by Alembic.
revision = "e312cfb04cf7"
down_revision = None
branch_labels = ("misago",)
depends_on = None

cache_versions = ("settings", "acl", "categories")


def upgrade():
    op.create_table(
        "misago_cache_versions",
        sa.Column("cache", sa.String(length=32), nullable=False),
        sa.Column("version", sa.String(length=8), nullable=False),
        sa.PrimaryKeyConstraint("cache"),
    )
    for cache in cache_versions:
        version = generate_version_string()
        op.execute(
            f"INSERT INTO misago_cache_versions (cache, version) VALUES ('{cache}', '{version}')"
        )


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("misago_cache_versions")
    # ### end Alembic commands ###
