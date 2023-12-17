"""empty message

Revision ID: 5b0be0104a69
Revises: 
Create Date: 2023-08-26 20:20:58.902069

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5b0be0104a69'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('student',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('scores', sa.Text(), nullable=True),
    sa.Column('gender', sa.String(length=50), nullable=False),
    sa.Column('grading', sa.String(length=50), nullable=True),
    sa.Column('birthday', sa.DateTime(), nullable=False),
    sa.Column('birthplace', sa.String(length=50), nullable=False),
    sa.Column('address', sa.String(length=50), nullable=False),
    sa.Column('father_name', sa.String(length=500), nullable=True),
    sa.Column('mother_name', sa.String(length=500), nullable=True),
    sa.Column('father_job', sa.String(length=500), nullable=True),
    sa.Column('mother_job', sa.String(length=500), nullable=True),
    sa.Column('father_education', sa.String(length=500), nullable=True),
    sa.Column('mother_education', sa.String(length=500), nullable=True),
    sa.Column('nisn', sa.String(length=500), nullable=False),
    sa.Column('nik', sa.String(length=500), nullable=False),
    sa.Column('presention', sa.String(length=500), nullable=True),
    sa.Column('religion', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_student')),
    sa.UniqueConstraint('nik', name=op.f('uq_student_nik')),
    sa.UniqueConstraint('nisn', name=op.f('uq_student_nisn'))
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=50), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password', sa.String(length=500), nullable=False),
    sa.Column('role', sa.String(length=60), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_user')),
    sa.UniqueConstraint('email', name=op.f('uq_user_email')),
    sa.UniqueConstraint('username', name=op.f('uq_user_username'))
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    op.drop_table('student')
    # ### end Alembic commands ###