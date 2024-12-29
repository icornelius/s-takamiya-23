# This Python script validates the XML file 'transcription-takamiya-23.xml'
# against the Relax NG schema file 'takamiya-23.rnc'. The schema file is first
# converted to XML format. Run the script from the root directory.

from lxml import etree
import rnc2rng

xml_filename = 'transcription-takamiya-23.xml'
rnc_filename = 'takamiya-23.rnc'
logfile = 'errors.txt'

def validate_xml_with_rng(xml_filename, rnc_filename):
    print(f'Validating XML file {xml_filename} with {rnc_filename}')
    try:
        # Convert rnc to rng
        # h/t https://github.com/djc/rnc2rng/issues/43#issuecomment-1776963112
        rng_data = rnc2rng.load(rnc_filename)
        rngxml = rnc2rng.dumps(rng_data).encode()

        # Parse the RNG schema
        schema = etree.RelaxNG(etree.fromstring(rngxml))

        # Parse the XML file

        xml_tree = etree.parse(xml_filename)
        
        # Validate the XML file against the schema
        if schema.validate(xml_tree):
            print("The XML file is valid according to the Relax NG schema.")
        else:
            print("The XML file is invalid.")
            print("\nValidation errors:")
            print(schema.error_log)
            with open(logfile, 'w') as f:
                f.write(str(schema.error_log))
    except Exception as e:
        print(f"An error occurred: {e}")

validate_xml_with_rng(xml_filename, rnc_filename)
