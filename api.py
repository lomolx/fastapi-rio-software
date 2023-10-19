import fastapi
import pydantic
import datetime as dt

app = fastapi.FastAPI()

MOVIES = [
    {
        "id": "120",
        "original_language": "English",
        "overview": "Young hobbit Frodo Baggins, after inheriting a mysterious ring from his uncle Bilbo, must leave his home in order to keep it from falling into the hands of its evil creator. Along the way, a fellowship is formed to protect the ringbearer and make sure that the ring arrives at its final destination: Mt. Doom, the only place where it can be destroyed.",
        "poster_path": "/6oom5QYQ2yQTMJIbnvbkBL9cHo6.jpg",
        "release_date": "2001-12-18",
        "runtime": 179,
        "tagline": "One ring to rule them all",
        "title": "The Lord of the Rings: The Fellowship of the Ring",
        "certification": "PG-13",
        "trailer": "https://www.youtube.com/watch?v=V75dMMIW2B4",
    },
    {
        "id": "603",
        "original_language": "English",
        "overview": "Set in the 22nd century, The Matrix tells the story of a computer hacker who joins a group of underground insurgents fighting the vast and powerful computers who now rule the earth.",
        "poster_path": "/f89U3ADr1oiB1s9GkdPOEpXUk5H.jpg",
        "release_date": "1999-03-30",
        "runtime": 136,
        "tagline": "Welcome to the Real World.",
        "title": "The Matrix",
        "certification": "R",
        "trailer": "https://www.youtube.com/watch?v=m8e-FF8MsqU",
        "directors":[{"id":"1","name":"juan","family_name":"tamayo"}]
    },
    {
        "id": "1368",
        "original_language": "English",
        "overview": "When former Green Beret John Rambo is harassed by local law enforcement and arrested for vagrancy, the Vietnam vet snaps, runs for the hills and rat-a-tat-tats his way into the action-movie hall of fame. Hounded by a relentless sheriff, Rambo employs heavy-handed guerilla tactics to shake the cops off his tail.",
        "poster_path": "/fVamGe8rfEQUrMbzumL1t0DslCA.jpg",
        "release_date": "1982-10-22",
        "runtime": 93,
        "tagline": "This time he's fighting for his life.",
        "title": "First Blood",
        "certification": "R",
        "trailer": "https://www.youtube.com/watch?v=IAqLKlxY3Eo",
    },
    {
        "id": "218",
        "original_language": "English",
        "overview": 'In the post-apocalyptic future, reigning tyrannical supercomputers teleport a cyborg assassin known as the "Terminator" back to 1984 to kill Sarah Connor, whose unborn son is destined to lead insurgents against 21st century mechanical hegemony. Meanwhile, the human-resistance movement dispatches a lone warrior to safeguard Sarah. Can he stop the virtually indestructible killing machine?',
        # "poster_path": "/qvktm0BHcnmDpul4Hz01GIazWPr.jpg",
        "release_date": "1984-10-26",
        "runtime": 108,
        "tagline": "Your future is in his hands.",
        "title": "The Terminator",
        "certification": "R",
        "trailer": "https://www.youtube.com/watch?v=k64P4l2Wmeg",
    },
]

class Director(pydantic.BaseModel):
    id:str
    name:str
    family_name: str

class Movie(pydantic.BaseModel):
    id: str
    title: str
    poster_path: str | None = None
    runtime: int
    release_date: dt.date
    directors: list[Director] = []


@app.get("/movies")
async def movies(title: str | None = None, query: str | None = None)->list[Movie]:
    result = MOVIES
    if title is not None:
        print(f"filtering by title: {title}")
        result = [m for m in result if title.lower() in m["title"].lower()]
        print(f"result after filter by title: {result}")
    if query is not None:
        print(f"filtering by query: {query}")
        result = [m for m in result if query.lower() in m["overview"].lower()]
        print(f"result after filter by query: {result}")
    result=[m|{"release_date": dt.date.fromisoformat(m["release_date"])} for m in result ]
    return result 
