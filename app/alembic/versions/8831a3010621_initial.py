"""initial

Revision ID: 8831a3010621
Revises: 
Create Date: 2024-11-15 14:12:53.563441

"""
from typing import Sequence, Union
import sqlmodel.sql.sqltypes
import sqlmodel
from alembic import op
import sqlalchemy as sa



# revision identifiers, used by Alembic.
revision: str = '8831a3010621'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('prophecy',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('content', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('used', sa.Boolean, nullable=False, default=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('prophecy')
    # ### end Alembic commands ###
