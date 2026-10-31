# Cookie Auditor

Review copied Set-Cookie header lines for common security attributes.

## Requirements
Python 3.10+, standard library only.

## Usage
`python cookie_auditor.py --help`

Supply a local text export or copied response headers. This tool is passive: it does not contact websites or alter configuration. Findings are advisory and require review in context.

## Tests
`python -m unittest discover -s tests -v`
