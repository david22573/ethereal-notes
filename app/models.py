from sqlmodel import Field, Relationship, SQLModel


class Notebook(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    description: str | None

    parent_id: int | None = Field(default=None, foreign_key="notebook.id")
    parent: "Notebook" = Relationship(
        back_populates="children",
        sa_relationship_kwargs={"remote_side": "Notebook.id", "single_parent": True},
    )

    children: list["Notebook"] = Relationship(
        back_populates="parent", cascade_delete=True
    )

    notes: list["Note"] = Relationship(back_populates="notebook", cascade_delete=True)


class Note(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str
    content: str

    notebook_id: int | None = Field(default=None, foreign_key="notebook.id")
    notebook: Notebook | None = Relationship(back_populates="notes")


def create_db_and_tables(engine):
    SQLModel.metadata.create_all(engine)
