from sqlmodel import Field, Relationship, SQLModel


class Notebook(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    description: str | None

    parent_id: int | None = Field(default=None, foreign_key="notebook.id")
    parent: "Notebook" | None = Relationship(
        back_populates="children",
        sa_relationship_kwargs={"remote_side": "Notebook.id"},
        cascade_delete=True,
        passive_deletes="all",
    )

    children: list["Notebook"] = Relationship(
        back_populates="parent", cascade_delete=True, passive_deletes="all"
    )

    notes: list["Note"] = Relationship(
        back_populates="notebook", cascade_delete=True, passive_deletes="all"
    )


class Note(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str
    content: str

    notebook_id: int | None = Field(
        default=None, foreign_key="notebook.id", on_delete="CASCADE"
    )
    notebook: Notebook | None = Relationship(back_populates="notes")
