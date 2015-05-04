from setuptools import setup

setup(
    name = "change-genbank-origin",
    version = "0.0.1",
    author = "Haydn King",
    author_email = "hjking734@gmail.com",
    description = ("A quick, dirty python script to change the point of " +
			"reference of a genbank plasmid DNA sequence file"),
    license = "BSD",
    scripts = [
        'scripts/change-genbank-origin'
    ]
)

