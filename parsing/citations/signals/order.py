# Structure and Use of Legal Citations: 
#   Order of Signals
#
# Source: 
#  The Bluebook 18th Ed. (2008). p48-51 (R1)
#
# 

import .definitions

########################################
# (rule 1.3)
# Order of Signals
#
# The BB states that the order of signals should be in accordance to
# their order in rule 1.2 and that the cited authorities must conform
# to rule 1.4.
########################################
 
ordered_signals = [
    NO_SIGNAL,
    EG,
    ACCORD,
    SEE,
    SEE_ALSO,
    CF,
    COMPARE,
    WITH,
    CONTRA,
    BUT_SEE,
    BUT_CF,
    SEE_GENERALLY
]


########################################
# (rule 1.4)
# Order of Authorities within each Signal
#
# - Authorities within each signal should be separated by a semicolon.
#
# - Authorities within signals should follow the list below. 
#
#     - Except if an authority is considerably (decisively) more
#       authoritative within a signal then it should precedes the
#       others.
########################################

orderd_authorities = [

    # (rule 1.4.a) 
    # Constitutions 
    # -----------------
    # 1. federal
    # 2. state (alphabetical by state)
    # 3. foreign (alphabetical by jurisdiction)
    # 4. Founding documents of (in order):
    #     i.  United Nations
    #    ii.  League of Nations
    #   iii.  European Union

    # (rule 1.4.b)
    # Statues
    # -----------------
    #
    # FEDERAL 
    # *******
    # 1. U.S.C., U.S.C.A, or U.S.C.S. (in +order of U.S.C title)
    # 2. Statues in force but not in authorities listed above
    #    (-chronological order of enactment)
    # 3. rules of evidence or procedure 
    # 4. repealed statutes (-chronological order of enactment)
    #
    # States (Alpha by state)
    # ***********************
    # 5. statutes in current codification (+order of codication)
    # 6. statutes currently in force but not in the current
    #    codification (-chronological order of enactment)
    # 7. rules of evidence or procedure 
    # 8. Repealed statutes (-chronological order of enactment)
    #
    # Foriegn (Alpha by jurisdiction)
    # *******************************
    # 9. codes statutes in current codification (+order of codication)
    # 10. statutes currently in force but not in the current
    #    codification (-chronological order of enactment)
    # 11. Repealed statutes (-chronological order of enactment)

    # (rule 1.4.c) not too important
    # Treaties and other international agreements

    # (rule 1.4.d) very important
    # Cases
    
    # (rule 1.4.e) important
    # Legislative materials
    
    # (rule 1.4.f) important
    # Administrative and Executive Materials
    
    # (rule 1.4.g) not important
    # Resolutions, decisions, and regulations of intergovernmental organizations
    
    # (rule 1.4.h) probably important
    # Records, Briefs, Petitions

    # (rule 1.4.i) important
    # Secondary Materials

    # (rule 1.4.j) maybe important
    # Cross-references
]
