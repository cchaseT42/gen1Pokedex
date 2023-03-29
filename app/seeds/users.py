from app.models import db, User, Pokemon, environment, SCHEMA
from sqlalchemy.sql import text


# Adds a demo user, you can add other users here if you want
def seed_users():
    demo = User(
        username='Demo', email='demo@aa.io', password='password')
    marnie = User(
        username='marnie', email='marnie@aa.io', password='password')
    bobbie = User(
        username='bobbie', email='bobbie@aa.io', password='password')

    db.session.add(demo)
    db.session.add(marnie)
    db.session.add(bobbie)
    db.session.commit()

    pokemon1 = Pokemon(
        id = 0o01, name="Bulbasaur", evolutions="Ivysaur, Venusaur", evo_level=16,
        moves="Level 1 Tackle, Level 1 Growl, Level 7 Leech Seed, Level 13 Vine Whip, Level 20 Poison Powder, Level 27 Razor Leaf, Level 34 Growth, Level 41 Sleep Powder, Level 48 SolarBeam",
        types="Grass/Poison",
        locations="Starter Pokemon"
    )

    pokemon2 = Pokemon(
        id=0o02, name="Ivysaur", evolutions="Venusaur", evo_level=32,
        moves="Level 1 Tackle, Level 1 Growl, Level 7 Leech Seed, Level 13 Vine Whip, Level 22 Poison Powder, Level 30 Razor Leaf, Level 38 Growth, Level 46 Sleep Powder, Level 54 SolarBeam",
        types="Grass/Poison",
        locations="Evolve Bulbasaur"
    )

    pokemon3 = Pokemon(
        id=0o03, name="Venusaur", moves="Level 1 Tackle, Level 1 Growl, Level 7 Leech Seed, Level 13 Vine Whip, Level 22 Poison Powder, Level 30 Razor Leaf, Level 48 Growth, Level 55 Sleep Powder, Level 65 SolarBeam",
        types="Grass/Poison",
        locations="Evolve Ivysaur"
    )

    db.session.add(pokemon1)
    db.session.add(pokemon2)
    db.session.add(pokemon3)
    db.session.commit()

# Uses a raw SQL query to TRUNCATE or DELETE the users table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_users():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.users RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM users"))

    db.session.commit()
