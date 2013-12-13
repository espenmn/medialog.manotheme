def setupVanoous(context):

    # Ordinanoly, GenericSetup handlers check for the existence of XML files.
    # Here, we are not parsing an XML file, but we use this text file as a
    # flag to check that we actually meant for this import step to be run.
    # The file is found in profiles/default.

    if context.readDataFile('medialog.manotheme_vanoous.txt') is None:
        return

    # Add additional setup code here
