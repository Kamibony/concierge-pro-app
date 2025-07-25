"""Cria tabela inicial prestadores"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1edff9622563'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('prestadores',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(), nullable=True),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('telefone', sa.String(), nullable=True),
    sa.Column('categoria', sa.String(), nullable=True),
    sa.Column('especialidades', sa.JSON(), nullable=True),
    sa.Column('bairro', sa.String(), nullable=True),
    sa.Column('disponibilidade', sa.String(), nullable=True),
    sa.Column('observacao', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_prestadores_categoria'), 'prestadores', ['categoria'], unique=False)
    op.create_index(op.f('ix_prestadores_email'), 'prestadores', ['email'], unique=True)
    op.create_index(op.f('ix_prestadores_id'), 'prestadores', ['id'], unique=False)
    op.create_index(op.f('ix_prestadores_nome'), 'prestadores', ['nome'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_prestadores_nome'), table_name='prestadores')
    op.drop_index(op.f('ix_prestadores_id'), table_name='prestadores')
    op.drop_index(op.f('ix_prestadores_email'), table_name='prestadores')
    op.drop_index(op.f('ix_prestadores_categoria'), table_name='prestadores')
    op.drop_table('prestadores')
    # ### end Alembic commands ###
