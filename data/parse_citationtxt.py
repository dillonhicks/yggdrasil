from lxml import etree as ET

def preprocess(text):
    """
    convert the text into a list of line strings.
    """
    lines = text.splitlines()

    # strip whitespace
    lines = [l.strip() for l in lines]

    # kill comments 
    lines = filter(lambda l: not l.startswith('#'), lines)

    # filter out blank lines
    lines = filter(lambda l: len(l) > 0, lines)

    return lines


def build_data(lines):
    current_section = ""
    data = {}

    for line in lines:
        if not current_section or line in sections:
            current_section = line
            data[current_section] = {'citations' : [], 'comments' : []}
            continue
    
        if line.startswith('*'):
            data[current_section]['comments'].append(line)
            continue
        
        data[current_section]['citations'].append(line)
        
    return data


def build_xml(data):
    root = ET.Element("CitationData")
    for section, elems in data.items():
        sect_node = ET.SubElement(root, "Section")
        sect_node.set("id", section);
        for cite in elems['citations']:
            cite_node = ET.SubElement(sect_node, "Citation")
            cite_node.text = cite
        for comment in elems['comments']:
            comment_node = ET.SubElement(sect_node, "Comment")
            comment_node.text = comment
            
    return root


def main(filetext):
    lines = preprocess(filetext)
    data = build_data(lines)
    xml = build_xml(data)

    with open('citations.xml', 'w') as outfile:
        outfile.write(ET.tostring(xml, pretty_print=True, encoding="unicode"))


sections = ['Supreme Court',
 'Courts of Appeals',
 'District Courts',
 'Court of Federal Claims',
 'Bankruptcy Courts and Bankruptcy Panels',
 'Tax Court',
 'Military Service Courts of Criminal Appeals',
 'Alabama',
 'Alaska',
 'Arizona',
 'Arkansas',
 'California',
 'Colorado',
 'Connecticut',
 'Delaware',
 'District of Columbia',
 'Florida',
 'Georgia',
 'Hawaii',
 'Idaho',
 'Illinois',
 'Indiana',
 'Iowa',
 'Kansas',
 'Louisiana',
 'Maine',
 'Maryland',
 'Massachusetts',
 'Michigan',
 'Minnesota',
 'Mississippi',
 'Missouri',
 'Montana',
 'Nebraska',
 'Nevada',
 'New Hampshire',
 'New Jersey',
 'New Mexico',
 'New York',
 'North Carolina',
 'North Dakota',
 'Ohio',
 'Oklahoma',
 'Oregon',
 'Pennsylvania',
 'South Carolina',
 'South Dakota',
 'Tennessee',
 'Texas',
 'Utah',
 'Vermont',
 'Virginia',
 'Washington',
 'West Virginia',
 'Wisconsin',
 'Wyoming']


citationtxt_contents = """
#
# Source: http://www.law.cornell.edu/citation/ 
# Accessed: Nov. 30, 2012
#
 
Supreme Court	
Brown v. Helvering, 291 U.S. 193, 203 (1934).

John Doe Agency v. John Doe Corp., 493 U.S. 146, 159-60 (1934) (Stevens, J., dissenting).

Cornish v. D.C. Bd. on Prof'l Responsibility, 117 S. Ct. 547, 136 L. Ed. 2d 430 (1996).

Cammisano v. U.S. Senate Permanent Subcomm. on Investigations, 454 U.S. 1084 (1981).

Office of Pers. Mgmt. v. Richmond, 496 U.S. 414 (1990).

Scott v. Harris, 127 S. Ct. 1769 (2007).

Lawrence v. Florida, 166 L. Ed. 2d 924 (2007).

Scott v. Harris, 75 U.S.L.W. 4297 (U.S. Apr. 30, 2007).

Courts of Appeals	
Shames v. Cal. Travel & Tourism Op. Comm'n, 607 F.3d 611 (9th Cir. 2010).

Antonov v. Cnty. of Los Angeles Dep't of Pub. Soc. Servs., 103 F.3d 137 (9th Cir. 1996).

Chatchka v. Soc'y for Concerned Citizens Interested in Equal., 69 F.3d 666 (5th Cir. 1996).

Comm. to Prevent Mun. Bankr. v. Renne, 77 F.3d 488 (9th Cir. 1996).

Cong. Fin. v. Commercial Tech., Inc., 74 F.3d 1253 (11th Cir. 1995).

Shoemaker v. Accreditation Council for Graduate Med. Educ., 87 F.3d 1322 (9th Cir. 1996).

Natural Res. Def. Council v. NRC, 216 F.3d 1180 (D.C. Cir. 2000).

Wilson v. Mar. Overseas Corp., 150 F.3d 1 (1st Cir. 1998).

Phillips Exeter Acad. v. Howard Phillips Fund, Inc., 196 F.3d 284 (1st Cir. 1999).

Grace Bible Fellowship, Inc. v. Me. Sch. Admin. Dist. No. 5, 941 F.2d 45 (1st Cir. 1991).

A.B.C. Bus Lines v. Urban Mass Transp. Admin., 831 F.2d 360 (1st Cir. 1987).

Orange County Agric. Soc'y, Inc. v. Comm'r, 893 F.2d 529 (2d Cir. 1990).

Shiau v. U.S. Dep't of Agric., 895 F.2d 1410 (2d Cir. 1989).

S'holders v. Sound Radio, 109 F.3d 873 (3d Cir. 1997).

Barry v. Bergen County Prob. Dep't, 128 F.3d 152 (3d Cir. 1997).

Tillman v. Lebanon County Corr. Facility, 221 F.3d 410 (3d Cir. 2000).

Johnstone v. N. Am. Van Lines, 958 F.2d 363 (3d Cir. 1992).

Opticians Ass'n of Am. v. Indep. Opticians of Am., 920 F.2d 187 (3d Cir. 1990).

Little Princess Assocs. v. Passgo, Inc. 922 F.2d 832 (3d Cir. 1990).

Philadelphia Marine Trade Ass'n v. Local 1242, Int'l Longshoremen's Ass'n, 915 F.2d 1561 (3d Cir. 1990).

S.C. State Ports Auth. v. NLRB, 914 F.2d 49 (4th Cir. 1990).

Gulf Atl., Inc. v. Gen. Elec. Co., 878 F.2d 1430 (4th Cir. 1989).

Stewart Glass & Mirror, Inc. v. U.S. Auto Glass Disc. Ctrs., Inc., 200 F.3d 307 (5th Cir. 2000).

Cobb v. Delta Exps., Inc., 186 F.3d 675 (5th Cir. 1999).

Moore v. U.S. Auto. Ass'n, 800 F.2d 1147 (5th Cir. 1987).

BAW Mfg. Co. v. Slaks Fifth Ave., Ltd., 547 F.2d 928 (5th Cir. 1977).

United States ex rel. Interstate Mech. Contrs., Inc. v. Int'l Fid. Ins. Co., 200 F.3d 456 (6th Cir. 2000).

Wooddell v. Int'l Bhd. of Elec. Workers, Local 71, 907 F.2d 151 (6th Cir. 1990), rev'd 112 S. Ct. 494 (1991).

NLRB v. Dist. 29, 921 F.2d 645 (6th Cir. 1990).

Schoonover v. Black Bros. Co., 914 F.2d 258 (6th Cir. 1990).

Buchanan v. Apfel, 249 F.3d 485, 2001 FED App. 0138P (6th Cir.).

Kennedy v. Nat'l Juvenile Det. Ass'n, 187 F.3d 690 (7th Cir. 1999).

Travis v. Gary Cmty. Mental Health Ctr., 921 F.2d 108 (7th Cir. 1990), cert. denied, 112 S. Ct. 60 (1991).

A.G. Edwards & Sons, Inc. v. Pub. Bldg. Comm'n, 921 F.2d 118 (7th Cir. 1990).

Trs. of Cent. States Health & Welfare Fund v. Lamberti, 878 F.2d 384 (7th Cir. 1989).

Hair v. Helena Chem. Co., 915 F.2d 1579 (8th Cir. 1990).

Mo. Hous. Dev. Comm'n v. Brice, 919 F.2d 1306 (8th Cir. 1990).

Ark. State Bank Comm'r v. Resolution Trust Corp., 911 F.2d 161 (8th Cir. 1990).

Crain v. Bd. of Police Comm'rs of the Metro. Police Dep't, 920 F.2d 1402 (8th Cir. 1990).

Am. Prof'l Testing Serv. v. Harcourt Brace Jovanovich Legal & Prof'l Publ'ns, 108 F.3d 1147 (9th Cir. 1997).

Benton Franklin Riverfront Trailway & Bridge Comm. v. Skinner, 914 F.2d 1496 (9th Cir. 1990).

Ins. Co. of Pa. v. Associated Int'l Ins. Co., 922 F.2d 516 (9th Cir. 1990)

Morrell Constr. v. Home Ins. Co., 920 F.2d 576 (9th Cir. 1990).

Olguin v. Inspiration Consol. Copper Co., 740 F.2d 1468 (9th Cir. 1984).

Dillon v. Fibreboard Corp., 919 F.2d 1488 (10th Cir. 1990).

Commc'n Workers of Am. v. Southeastern Elec. Coop., 882 F.2d 467 (10th Cir. 1989).

Haagen-Dazs Co. v. Masterbrand Distribs., 918 F.2d 183 (11th Cir. 1990).

Tally-Ho, Inc. v. Coast Cmty. Coll. Dist., 889 F.2d 1018 (11th Cir. 1989).

Nat'l Distrib. Co. v. James B. Beam Distilling Co. 845 F.2d 307 (11th Cir. 1988).

Court of Appeals for the Federal Circuit	Or. Steel Mills, Inc. v. United States, 862 F.2d 1541 (Fed. Cir. 1988).
District Courts	
Hollander v. Inst. For Research on Women & Gend. At Columbia Univ., No. 08 Civ. 7286 (LAK) (KNF), 2009 U.S. Dist. LEXIS 34942 (S.D.N.Y. Apr. 15, 2009).

Huangyan Imp. & Exp. Corp. v. Nature's Farm Prods., No. 99 Civ. 9404 (SHS), 2000 U.S. Dist. LEXIS 12335 (S.D.N.Y. Aug. 25, 2000).

Villar v. Crowley Mar. Corp., 780 F. Supp. 1467 (S.D. Tex. 1992).

Diaz v. Antilles Conversion & Exp., Inc., 62 F. Supp. 2d 463 (D.P.R. 1999).

Glen Holly Entm't, Inc. v. Tektronix, Inc., 100 F. Supp. 2d 1073 (C.D. Cal. 1999).

Perlman v. Swiss Bank Corp. Comprehensive Disability Prot. Plan, 979 F. Supp. 726 (N.D. Ill. 1997).

Natural Res. Def. Council v. Fox, 93 F. Supp. 2d 531 (S.D.N.Y. 2000).

Chatoff v. West Publ'g Co., 948 F. Supp. 176 (E.D.N.Y. 1996).

Haghighi v. Russian-American Broad. Co., 945 F. Supp. 1233 (D. Minn. 1996).

Upjohn Co. v. Mova Pharm. Corp., 936 F. Supp. 55 (D.P.R. 1996).

N.J. Tpk. Auth. v. PPG Indus., 16 F. Supp. 2d 460 (D.N.J. 1998).

Trs. of the Univ. of Pa. v. Mayflower Transit, Civil Action No. 97-1111, 1997 U.S. Dist. LEXIS 14577, (E.D. Pa. Sept. 16, 1997).

Azalea Meats, Inc. v. Muscat, 246 F. Supp. 780 (S.D. Fla. 1965).

Glinsey v. Baltimore & O.R.R., 356 F. Supp. 984 (N.D. Ohio 1973), rev'd, 495 F.2d 565 (6th Cir. 1974).

Post v. Textron, Inc., 554 F. Supp. 419 (W.D. Mich. 1983).

Hotchner v. Barrymore, 31 F. Supp. 928 (E.D.N.Y. 1940).

Lamkin v. Bowen, 721 F. Supp. 263 (D. Colo. 1989).

Allen v. Hunter, 65 F. Supp. 365 (D. Kan. 1946).

Navajo Freight Lines v. Bibb, 159 F. Supp. 385 (S.D. Ill. 1958).

McRae v. Publ'ns Int'l, 985 F. Supp. 1036 (D. Kan. 1997).

Van Houten v. Ralls, 290 F. Supp. 67 (D. Nev. 1967).

United States v. Love, 141 F.R.D. 315 (D. Colo. 1992).

Court of Federal Claims	
Ex'r of Estate of Wicker v. United States, 43 Fed. Cl. 172 (1999).

Express Foods, Inc. v. United States, 229 Ct. Cl. 733 (Cl. Ct. 1981).*

Youngstown Steel Equip. Sales, Inc. v. United States, 20 Cl. Ct. 517 (1990), rev'd, 935 F.2d 281 (Fed. Cir. 1991).

The parenthetical reference "Cl. Ct." must be included in pre-1982 cites to the Ct. Cl. reporter but is unnecessary in cases cited to the Cl. Ct. reporter.

Bankruptcy Courts and Bankruptcy Panels	
Weiner v. Perry, Settles & Lawson, Inc., 208 B.R. 69 (B.A.P. 1st Cir. 1997).

Tax Court	
Allied Equip. Leasing II v. Comm'r, 97 T.C. 575 (1991).

Military Service Courts of Criminal Appeals	
United States v. Zamberlan, 45 M.J. 491 (C.A.A.F. 1997).

United States v. Myers, 25 M.J. 573 (A.F.C.M.R. 1987), petition denied, 27 M.J. 20 (C.M.A. 1988).

United States v. Young, 24 M.J. 626 (A.C.M.R. 1987).

 

State Case Citations:

In states where a citation variant appears against a different background there is a distinct case citation format used within the jurisdiction by state courts and those submitting memoranda or briefs to them.

Alabama	Illinois	Montana	Rhode Island
Alaska	Indiana	Nebraska	South Carolina
Arizona	Iowa	Nevada	South Dakota
Arkansas	Kansas	New Hampshire	Tennessee
California	Kentucky	New Jersey	Texas
Colorado	Louisiana	New Mexico	Utah
Connecticut	Maine	New York	Vermont
Delaware	Maryland	North Carolina	Virginia
District of Columbia	Massachusetts	North Dakota	Washington
Florida	Michigan	Ohio	West Virginia
Georgia	Minnesota	Oklahoma	Wisconsin
Hawaii	Mississippi	Oregon	Wyoming
Idaho	Missouri	Pennsylvania	 
 

Alabama	
Se. Meats of Pelham, Inc. v. City of Birmingham, 895 So. 2d 909 (Ala. 2004).

Talton Telecomm. Corp. v. Coleman, 665 So. 2d 914 (Ala. 1995).

Piersol v. ITT Phillips Drill Div., Inc., 445 So. 2d 559 (Ala. 1989).

Mims v. Am. Fed'n of Gov't Empls., 531 So. 2d 661 (Ala. 1988).

Gov't & Civic Empls. Org. Comm. v. Windsor, 262 Ala. 285, 78 So. 2d 646 (1955).*

Gov't & Civic Empls. Org. Comm. v. Windsor, 78 So. 2d 646 (Ala. 1955).

State Dep't of Pub. Health v. Boackle-Phipps Foods, 594 So. 2d 1234 (Ala. Civ. App. 1991).

Tracy v. Tracy, 939 So. 2d 48 (Ala. Civ. App. 2006).

Sanders v. State, 947 So. 2d 432 (Ala. Crim. App. 2006).

* Publication of Alabama Reports and Alabama Appellate Court Reports (Ala. App.) ceased in 1976. In-state references to decisions appearing in those reports should, where possible, include parallel citations to them. Note that Alabama has two intermediate appellate courts, one with civil and one with criminal jurisdiction.

Alaska	
Alaska Far E. Corp. v. Newby, 630 P.2d 533 (Alaska 1981).

Parks v. State, 731 P.2d 597 (Alaska Ct. App. 1987).

Parks v. State, 731 P.2d 597 (Alaska App. 1987).*

* In-state references to Alaska Court of Appeals decisions generally use this slightly more economical format. For more examples, see § 7-500.

Arizona	
Tom Reed Gold Mines Co. v. United E. Mining Co., 39 Ariz. 533, 8 P.2d 449 (1932).*

Tom Reed Gold Mines Co. v. United E. Mining Co., 8 P.2d 449 (Ariz. 1932).

Spurlock v. Santa Fe Pac. R.R. Co., 143 Ariz. 469, 694 P.2d 299 (Ct. App. 1984).*

Spurlock v. Santa Fe Pac. R.R. Co., 143 Ariz. 469, 694 P.2d 299 (App. 1984).**

Spurlock v. Santa Fe Pac. R.R. Co., 694 P.2d 299 (Ariz. Ct. App. 1984).

Johnson Int'l, Inc. v. City of Phoenix, 192 Ariz. 466, 470-71 ¶ 26, 967 P.2d 607, 611-12 (App. 1998).**

Johnson Int'l, Inc. v. City of Phoenix, 967 P.2d 607, 611-12 (Ariz. Ct. App. 1998).

* In-state references to decisions appearing in Arizona Reports should, where possible, include parallel citations to those reports.

** In-state references also generally use this slightly more economical abbreviation of the Court of Appeals. In addition, decisions rendered since January 1, 1998, include paragraph numbers which are generally used, together with rather than instead of page numbers, in in-state pinpoint citations. For more examples, see § 7-500.

Arkansas	
Whiteside v. Russellville Newspapers, Inc., 2009 Ark. 135, 295 S.W.3d 798.*

Whiteside v. Russellville Newspapers, Inc., 295 S.W.3d 798 (Ark. 2009).

Magnolia Sch. Dist. No. 14 v. Ark. State Bd. of Educ., 303 Ark. 666, 799 S.W.2d 791 (1990).*

Magnolia Sch. Dist. No. 14 v. Ark. State Bd. of Educ., 799 S.W.2d 791 (Ark. 1990).

All City Glass & Mirror v. McGraw Hill Info. Sys. Co., 295 Ark. 520, 750 S.W.2d 395 (1988).*

All City Glass & Mirror v. McGraw Hill Info. Sys. Co., 750 S.W.2d 395 (Ark. 1988).

Bronakowski v. Lindhurst, 2009 Ark. App. 513, 324 S.W.3d 719.*

Bronakowski v. Lindhurst, 324 S.W.3d 719 (Ark. 1990).

Aetna Cas. & Sur. Co. v. Dyer, 6 Ark. App. 211, 639 S.W.2d 536 (1982).*

Aetna Cas. & Sur. Co. v. Dyer, 639 S.W.2d 536 (Ark. Ct. App. 1982).

* In-state references to decisions appearing in Arkansas Reports should, where possible, include parallel citations to those reports. Citations to decisions from 2009 on should instead use the state's medium-neutral citation system.

California	
Green v. State of California, 42 Cal. 4th 254, 260, 165 P.3d 118, 121, 64 Cal. Rptr. 3d 390, 393 (2007).*

(Green v. State of California (2007) 42 Cal.4th 254, 260.)**

Green v. State of California, 165 P.3d 118, 121 (Cal. 2007).

Coal. of Concerned Cmtys., Inc. v. City of Los Angeles, 34 Cal. 4th 733, 101 P.3d 563, 21 Cal. Rptr. 3d 676 (2005).*

Coal. of Concerned Cmtys., Inc. v. City of Los Angeles, 101 P.3d 563 (Cal. 2005).

Cal. Educ. Facilities Auth. v. Priest, 12 Cal. 3d 593, 526 P.2d 513, 116 Cal. Rptr. 361 (1974).*

Cal. Educ. Facilities Auth. v. Priest, 526 P.2d 513 (Cal. 1974).

Sakotas v. Workers' Comp. Appeals Bd., 80 Cal. App. 4th 262, 95 Cal. Rptr. 2d 153 (2000).*

Sakotas v. Workers' Comp. Appeals Bd., 95 Cal. Rptr. 2d 153 (Ct. App. 2000).

Salinas v. Atchison, Topeka & Santa Fe Ry. Co., 5 Cal. App. 4th 1, 6 Cal. Rptr. 2d 446 (1992).*

Salinas v. Atchison, Topeka & Santa Fe Ry. Co., 6 Cal. Rptr. 2d 446 (Ct. App. 1992).

* In-state references to decisions appearing in California Reports or California Appellate Reports should, where possible, include parallel citations to them.

** In addition, they may but need not use the distinctive format employed by the California courts and set out in the California Style Manual. For examples, see § 7-500.

Colorado	
People v. Padilla-Lopez, 2012 CO 49, ¶ 18, 279 P.3d 651.*

People v. Padilla-Lopez, 279 P.3d 651, 656 (Colo. 2012).

City of Greeley v. Poudre Valley Rural Elec., 744 P.2d 739 (Colo. 1987), appeal dismissed, 485 U.S. 949 (1988).

B.K. Sweeney Elec. Co. v. Poston, 110 Colo. 139, 132 P.2d 443 (1942).*

B.K. Sweeney Elec. Co. v. Poston, 132 P.2d 443 (Colo. 1942).

Vaccaro v. Am. Family Ins. Group, 2012 COA 9, ¶ 18, 275 P.3d 750.*

Vaccaro v. Am. Family Ins. Group, 275 P.3d 750 (Colo. Ct. App. 2012).

People v. Petschow, 119 P.3d 495 (Colo. App. 2004).*

People v. Petschow, 119 P.3d 495 (Colo. Ct. App. 2004).

Serv. Merch. Co. v. Schwartzberg, 971 P.2d 654 (Colo. Ct. App. 1997).

Vessels Oil & Gas Co. v. Coastal Ref. & Mktg., Inc., 764 P.2d 391 (Colo. Ct. App. 1988).

* Publication of Colorado Reports ceased in 1980. In-state references to decisions appearing in those reports should, where possible, include parallel citations to them. In addition, in-state references to decisions of the Court of Appeals can follow the practice of the Colorado courts and use a slightly more economic abbreviation of the court. For more examples, see § 7-500. Citations to decisions from 2012 on can use the state's medium-neutral citation system instead of citations to the regional reporter; they need not include a parallel citation.

Connecticut	
Tovish v. Gerber Elecs., 212 Conn. 814, 565 A.2d 538 (1989).*

Tovish v. Gerber Elecs., 565 A.2d 538 (Conn. 1989).

Hansen v. Ohio Cas. Ins. Co., 239 Conn. 549, 687 A.2d 1262 (1995).*

Hansen v. Ohio Cas. Ins. Co., 687 A.2d 1262 (Conn. 1995).

Vogel v. Maimonides Acad. of W. Conn., Inc., 58 Conn. App. 624, 754 A.2d 824 (2000).*

Vogel v. Maimonides Acad. of W. Conn., Inc.,� 754 A.2d 824 (Conn. App. Ct. 2000).

Chaleunphone v. Slater Rd. Assocs., 26 Conn. App. 946, 602 A.2d 47 (1992).*

Chaleunphone v. Slater Rd. Assocs., 602 A.2d 47 (Conn. App. Ct. 1992).

Bishop's Corner Assocs. Ltd. P'shp v. Serv. Merch. Co., 45 Conn. Supp. 443, 720 A.2d 531 (1997).*

Bishop's Corner Assocs. Ltd. P'shp v. Serv. Merch. Co., 720 A.2d 531 (Conn. Super. Ct. 1997).

* In-state references to decisions appearing in Connecticut Reports, Connecticut Appellate Reports, or Connecticut Supplement should, where possible, include citations to them. Indeed, state rules specify that citations in the argument portion of a brief should be to the official reports alone.

Delaware	
Reagan v. Del. Ass'n of Prof'l Eng'rs, 577 A.2d 755 (Del. 1990).

In re Polaroid Corp. S'holders Litig., 560 A.2d 491 (Del. 1989).

Istituto Bancario Italiano SpA v. Hunter Eng'g Co., 449 A.2d 210 (Del. 1981).

Bank of Am. Nat'l Trust & Sav. Assoc. v. GAC Props. Credit, Inc., 389 A.2d 1304 (Del. Ch. 1978).

District of Columbia	
Croom v. United States, 546 A.2d 1006 (D.C. 1988).

Lennon v. United States Theatre Corp., 287 U.S. App. D.C. 202, 920 F.2d 996 (1990).*

Lennon v. United States Theatre Corp., 920 F.2d 996 (D.C. Cir. 1990).

* References to decisions of the U.S. Court of Appeals for the D.C. Circuit in briefs submitted to D.C. courts should include citations to the United States Court of Appeals Reports in addition to the Federal Reporter.

Florida	
Swofford v. Richards Enters., Inc., 515 So. 2d 231 (Fla. 1987).

City of N. Miami v. Fla. Defenders of the Env't, 481 So. 2d 1196 (Fla. 1985).

Gore v. Space Sci. Servs., 697 So. 2d 841 (Fla. 1st DCA 1997).*

Gore v. Space Sci. Servs., 697 So. 2d 841 (Fla. Dist. Ct. App. 1997).

S.O.S. Reprod. Sys. of Tampa, Inc. v. Saxon Bus. Prods., Inc., 320 So. 2d 500 (Fla. 3d DCA 1975).*

S.O.S. Reprod. Sys. of Tampa, Inc. v. Saxon Bus. Prods., Inc., 320 So. 2d 500 (Fla. Dist. Ct. App. 1975).

* In-state references to decisions of the District Court of Appeal should indicate the district, and in similar fashion references to the Circuit Court should indicate the circuit and references to the County Court, the county. The format for doing so is set out in the Florida rules. For those rules and more examples, see § 7-500.

Georgia	
Retention Alts., Ltd. v. Hayward, 285 Ga. 437, 678 S.E.2d 877 (2009).*

Retention Alts., Ltd. v. Hayward, 678 S.E.2d 877 (Ga. 2009).

Dalcor Mgmt., Inc. v. Sewer Rooter, Inc., 423 S.E.2d 419 (Ga. Ct. App. 1992).

S & S Mach. Co. v. Intermar S.S. Corp., 189 Ga. App. 13, 374 S.E.2d 767 (1988).*

S & S Mach. Co. v. Intermar S.S. Corp., 374 S.E.2d 767 (Ga. Ct. App. 1988).

* In-state references to decisions appearing in Georgia Reports or Georgia Appeals Reports should, where possible, include citations to them.

Hawaii	
Pac. Concrete Fed. Credit Union v. Kauanoe, 62 Haw. 334, 614 P.2d 936 (1980).*

Pac. Concrete Fed. Credit Union v. Kauanoe, 614 P.2d 936 (Haw. 1980).

Krohnert v. Yacht Sys. Haw., Inc., 4 Haw. App. 190, 664 P.2d 738 (1983).*

Krohnert v. Yacht Sys. Haw., Inc., 664 P.2d 738 (Haw. Ct. App. 1983).

* In-state references to decisions appearing in Hawaii Reports or Hawaii Appellate Reports should, where possible, include citations to them. Hawaii Appellate Reports ended in 1994. Since 1994, Hawaii Reports have included decisions of both the Hawaii Supreme Court and the Hawaii Intermediate Court of Appeals.

Idaho	
Kootenai Envtl. Alliance, Inc. v. Panhandle Yacht Club, Inc., 105 Idaho 622, 671 P.2d 1085 (1983).*

Kootenai Envtl. Alliance, Inc. v. Panhandle Yacht Club, Inc., 671 P.2d 1085 (Idaho 1983).

McCorkle v. Nw. Mut. Life Ins. Co., 112 P.3d 838 (Idaho Ct. App. 2005).

Jones v. Mountain States Tel. & Tel. Co., 105 Idaho 520, 620 P.2d 1305 (Ct. App. 1983).*

Jones v. Mountain States Tel. & Tel. Co., 620 P.2d 1305 (Idaho Ct. App. 1983).

* In-state references to decisions appearing in Idaho Reports should, where possible, include citations to them.

Illinois	
Snyder v. Heidelberger, 2011 IL 111052, 953 N.E.2d 415.*

Snyder v. Heidelberger, 953 N.E.2d 415 (Ill. 2011).

Linden Bros. v. Practical Elec. & Eng'g Publ'g Co., 309 Ill. 132, 140 N.E. 874 (1923).*

Linden Bros. v. Practical Elec. & Eng'g Publ'g Co., 140 N.E. 874 (Ill. 1923).

People v. Hansen, 2011 IL App (2d) 081226, 952 N.E. 82.*

People v. Hansen, 952 N.E.2d 82 (Ill. App. Ct. 2011).

Lewis v. Rutland Twp., 359 Ill. App. 3d 1076, 824 N.E.2d 1213 (2005).*

Lewis v. Rutland Twp., 824 N.E.2d 1213 (Ill. App. Ct. 2005).

Jastram v. Lake Villa Sch. Dist. 41, 192 Ill. App. 3d 599, 549 N.E.2d 9 (1989).*

Jastram v. Lake Villa Sch. Dist. 41, 549 N.E.2d 9 (Ill. App. Ct. 1989).

* In-state references to decisions appearing in Illinois Reports or Illinois Appellate Court Reports should, where possible, include citations to them. Citations to decisions from 2011 on should instead use the state's medium-neutral citation system. Illinois court rules allow, but do not require, parallel citations to the North Eastern Reporter.

Indiana	
Slater v. Akron Exch. State Bank, 221 Ind. 497, 49 N.E.2d 344 (1943).*

Slater v. Akron Exch. State Bank, 49 N.E.2d 344 (Ind. 1943).

Lovko v. Lovko, 179 Ind. App. 1, 384 N.E.2d 166 (1978).*

Lovko v. Lovko, 384 N.E.2d 166 (Ind. Ct. App. 1978).

Arth Main St. Drugs, Inc. v. A-1 Beverage Comm'n, 404 N.E.2d 65 (Ind. Ct. App. 1980).

* Publication of Indiana Court of Appeals Reports ceased in 1979; Indiana Reports, in 1981. In-state references to decisions appearing in those reports should, where possible, include parallel citations to them.

Iowa	
Iowa Fed'n of Labor v. Iowa Dep't of Job Serv., 427 N.W.2d 443 (Iowa 1988).

City of Sioux City v. Bd. of Trs. of Fire Ret. Sys., 348 N.W.2d 643 (Iowa Ct. App. 1984).

Bates v. Quality Ready-Mix Co., 261 Iowa 696, 154 N.W.2d 852 (1967).*

Bates v. Quality Ready-Mix Co., 154 N.W.2d 852 (Iowa 1967).

* Publication of Iowa Reports ceased in 1968. In-state references to decisions appearing in those reports should, where possible, include parallel citations to them.

Kansas	
Farmers Ins. Co. v. Sw. Bell Tel. Co., 279 Kan. 976, 113 P.3d 258 (2005).*

Farmers Ins. Co. v. Sw. Bell Tel. Co., 113 P.3d 258 (Kan. 2005).

Cent. Fin. Co. v. Stevens, 221 Kan. 1, 558 P.2d 122 (1976).*

Cent. Fin. Co. v. Stevens, 558 P.2d 122 (Kan. 1976).

De Graeve v. Sw. Bell Tel. Co., 9 Kan. App. 2d 753, 687 P.2d 1380 (1984).*

De Graeve v. Sw. Bell Tel. Co., 687 P.2d 1380 (Kan. Ct. App. 1984).

* In-state references to decisions appearing in Kansas Reports or Kansas Court of Appeals Reports should, where possible, include citations to them.

Kentucky	Dep't of Revenue v. Isaac W. Bernheim Found., Inc., 505 S.W.2d 762 (Ky. 1974).
Cement Transp., Inc. v. Hodges, 505 S.W.2d 32 (Ky. App. 1974).*

Cement Transp., Inc. v. Hodges, 505 S.W.2d 32 (Ky. Ct. App. 1974).

Louisville Title Mortg. Co. v. Commonwealth, 299 Ky. 224, 184 S.W.2d 963 (1944).*

Louisville Title Mortg. Co. v. Commonwealth, 184 S.W.2d 963 (Ky. Ct. App. 1944).

* In-state references should indicate the deciding court using this slightly different format set out in Kentucky rules.

Louisiana	
State v. Smith, 98-1417, p. 15 (La. 6/29/01); 793 So. 2d 1199, 1208.*

State v. Smith, 793 So. 2d 1199, 1208 (La. 2001).

Charles v. St. Mary Ironworks, Inc., 96-2923 (La. 3/14/97); 689 So. 2d 1380.*

Charles v. St. Mary Ironworks, Inc., 689 So. 2d 1380 (La. 1997).

Wilson v. Grosjean Contractors, Inc., 97-0012 (La. 3/14/97); 690 So. 2d 25.*

Wilson v. Grosjean Contractors, Inc., 690 So. 2d 25 (La. 1997).

Mellon Fin. Servs. Corp. #7 v. Alexander, 551 So. 2d 632 (La. 1989).

First Metro. Bank v. Plaia, 386 So. 2d 94 (La. 1980), on remand, 389 So. 2d 870 (La. Ct. App. 1980).

Economy Carpets Mfrs. v. Better Bus. Bureau, Inc., 341 So. 2d 555 (La. 1977).

Siemssen v. Manpower Temp. Servs., 95-80 (La.App. 5 Cir, 5/30/95); 656 So. 2d 1115.*

Siemssen v. Manpower Temp. Servs., 656 So. 2d 1115 (La. Ct. App. 1995).

Roberts v. La. State Univ. Med. Ctr., 554 So. 2d 230 (La. Ct. App. 1989).

* In-state references to decisions from 1994 forward should include a medium-neutral citation which, under Lousiana rules, consists of the docket number and date in the format shown here.

Maine	
Beale v. Sec'y of State, 1997 ME 82, ¶ 7, 693 A.2d 336.*

Beale v. Sec'y of State, 693 A.2d 336, 339 (Me. 1997).

Larochelle v. Hodsdon, 1997 ME 53, ¶ 13, 690 A.2d 986.*

Larochelle v. Hodsdon, 690 A.2d 986, 989 (Me. 1997).

Bazinet v. Concord Gen. Mut. Ins. Co., 513 A.2d 279 (Me. 1986).

* In-state references to decisions from 1997 forward should include a medium-neutral citation which, under Maine rules, consists of the year, the state postal abbreviation, and a sequential decision number in the format shown here. Pinpoint cites should be to the paragraph numbers assigned by the court.

Maryland	
Three Garden Vill. Ltd. P'ship v. United States Fid. & Guar. Co., 318 Md. 98, 567 A.2d 85 (1989).*

Three Garden Vill. Ltd. P'ship v. United States Fid. & Guar. Co., 567 A.2d 85 (Md. 1989).

Mclean Contracting Co. v. Md. Transp. Auth., 70 Md. App. 514, 521 A.2d 1251.*

Mclean Contracting Co. v. Md. Transp. Auth., 521 A.2d 1251 (Md. Ct. Spec. App.), cert. denied, 527 A.2d 51 (Md. 1987).

* In-state references to decisions appearing in Maryland Reports or Maryland Appellate Reports should, where possible, include citations to them. Note that the Maryland Court of Appeals is the state's highest court and the Maryland Court of Special Appeals, an intermediate appellate court.

Massachusetts	
WBZ-TV4 v. Exec. Office of Labor, 414 Mass. 767, 610 N.E.2d 923 (1993).*

WBZ-TV4 v. Exec. Office of Labor, 610 N.E.2d 923 (Mass. 1993).

McKenzie v. Brigham & Women's Hosp., 405 Mass. 432, 541 N.E.2d 325 (1989).*

McKenzie v. Brigham & Women's Hosp., 541 N.E.2d 325 (Mass. 1989).

Ne. Avionics, Inc. v. City of Westfield, 63 Mass. App. Ct. 509, 827 N.E.2d 721 (2005).*

Ne. Avionics, Inc. v. City of Westfield, 827 N.E.2d 721 (Mass. App. Ct. 2005).

Apahouser Lock & Sec. Corp. v. Carvelli, 25 Mass. App. Ct. 1117, 522 N.E.2d 1016 (1988).*

Apahouser Lock & Sec. Corp. v. Carvelli, 522 N.E.2d 1016 (Mass. App. Ct. 1988).

* In-state references to decisions appearing in Massachusetts Reports or Massachusetts Appeals Court Reports should, where possible, include citations to them.

Michigan	
Booker v Med Pers Pool, 456 Mich 913; 572 NW2d 656 (1997).*

Booker v. Med. Pers. Pool, 572 N.W.2d 656 (Mich. 1997).

Renshaw v Coldwater Hous Comm'n, 381 Mich 590; 165 NW2d 5 (1969).*

Renshaw v. Coldwater Hous. Comm'n, 165 N.W.2d 5 (Mich. 1969).

Nat'l Ctr for Mfg Scis v City of Ann Arbor, 221 Mich App 541; 563 NW2d 65 (1997).*

Nat'l Ctr. for Mfg. Scis. v. City of Ann Arbor, 563 N.W.2d 65 (Mich. Ct. App. 1997).

Gordon Food Serv, Inc v Grand Rapids Material Handling Co, 183 Mich App 241; 454 NW2d 137 (1989).*

Gordon Food Serv., Inc. v. Grand Rapids Material Handling Co., 454 N.W.2d 137 (Mich. Ct. App. 1989).

Med. Soc'y of NJ v NJ Dep't of Law & Pub Safety, 183 Mich App 241; 454 NW2d 137 (1989).*

Med. Soc'y of N.J. v. N.J. Dep't of Law & Pub. Safety, 454 N.W.2d 137 (Mich. Ct. App. 1989).

* In-state references to decisions appearing in Michigan Reports or Michigan Appeals Reports should, where possible, include citations to them, in parallel with citations to the regional reporter. The format shown above (including the absence of periods called for by The Bluebook and a semi-colon separating the parallel citations) is that set out in the Michigan rules. Those rules deviate in numerous other respects from the citation norms of The Bluebook for both Michigan and out-of-state authority. For those rules and more examples, see § 7-500.

Minnesota	
Minnegasco, Inc. v. Cnty. of Carver, 447 N.W.2d 878 (Minn. 1989).

Great W. Cas. Co. v. Christenson, 450 N.W.2d 153 (Minn. Ct. App. 1990).

Mississippi	
Blackledge v. Omega Ins. Co., 98-CA-00380-SCT (¶ 7), 740 So. 2d 295 (Miss. 1998) (en banc).*

Blackledge v. Omega Ins. Co., 740 So. 2d 295, 299 (Miss. 1998) (en banc).

ABC Mfg. Corp. v. Doyle, 97-CT-01376-SCT (¶ 14), 749 So. 2d 43 (Miss. 1997) (en banc).*

ABC Mfg. Corp. v. Doyle, 749 So. 2d 43, 46 (Miss. 1997) (en banc).

Hartford Accident & Indem. Co. v. Foster, 528 So. 2d 255 (Miss. 1988).

* In-state references to decisions from July 1, 1997, forward should include a medium-neutral citation which, under Mississippi rules, consists of the clerk-assigned case number in the format shown here. Pinpoint cites should be to the paragraph numbers assigned by the court.

Missouri	
Lewis v. St. Louis Indep. Packing Co., 3 S.W.2d 244 (Mo. 1928).

Ex rel. Dir. of Revenue, Mo. v. McKenzie, 936 S.W.2d 590 (Mo. Ct. App. 1996).

Imperial Util. Corp. v. Cytron, 673 S.W.2d 858 (Mo. Ct. App. 1984).

Montana	
Prescott v. Innovative Res. Grp., 2010 MT 35, ¶ 19, 355 Mont. 220, 225 P.3d 1253.*

Prescott v. Innovative Res. Grp., 225 P.3d 1253, 1256 (Mont. 2010).

Johnson v. Mont. Dep't of Labor & Indus., 240 Mont. 288, 783 P.2d 1355 (1989).*

Johnson v. Mont. Dep't of Labor & Indus., 783 P.2d 1355 (Mont. 1989).

* In-state references to decisions appearing in Montana Reports should, where possible, include citations to those reports, in parallel with citations to the regional reporter. In addition, in-state references to decisions from 1998 forward should include a medium-neutral citation which, under Montana rules, consists of the year, the state postal abbreviation, and a sequential decision number in the format shown here. Pinpoint cites should be to the paragraph numbers assigned by the court.

Nebraska	
NI Indus., Inc v. Husker-Hawkeye Distrib., Inc., 233 Neb. 808, 448 N.W.2d 157 (1989).*

NI Indus., Inc v. Husker-Hawkeye Distrib., Inc., 448 N.W.2d 157 (Neb. 1989).

Johnson v. Johnson, 15 Neb. App. 292, 726 N.W.2d 194 (2006).*

Johnson v. Johnson, 726 N.W.2d 194 (Neb. Ct. App. 2006).

* In-state references to decisions appearing in Nebraska Reports or Nebraska Court of Appeals Reports should, where possible, include citations to those reports.

Nevada	
Brisbin v. State Indus. Ins. Sys., 105 Nev. 1024, 810 P.2d 318 (1989).*

Brisbin v. State Indus. Ins. Sys., 810 P.2d 318 (Nev. 1989).

* In-state references to decisions appearing in Nevada Reports should, where possible, include citations to those reports.

New Hampshire	
Psychiatric Inst. of Am. v. Mediplex, Inc., 130 N.H. 125, 536 A.2d 169 (1987), later proceeding, 132 N.H. 177, 564 A.2d 818 (1989).*

Psychiatric Inst. of Am. v. Mediplex, Inc., 536 A.2d 169 (N.H. 1987), later proceeding, 564 A.2d 818 (N.H. 1989).

* In-state references to decisions appearing in New Hampshire Reports should, where possible, include citations to those reports.

New Jersey	
Dep't of Envtl. Prot. v. Lennan, 147 N.J. 579, 688 A.2d 1055 (1997).*

Dep't of Envtl. Prot. v. Lennan, 688 A.2d 1055 (N.J. 1997).

Essex Cnty. Welfare Bd. v. Dep't of Insts. & Agencies, 75 N.J. 232, 381 A.2d 349 (1978).*

Essex Cnty. Welfare Bd. v. Dep't of Insts. & Agencies, 381 A.2d 349 (N.J. 1978).

Diehl v. Diehl, 389 N.J. Super. 443, 913 A.2d 803 (App. Div. 2006).*

Diehl v. Diehl, 913 A.2d 803 (N.J. Super. Ct. App. Div. 2006).

Davis v. City of Plainfield, 389 N.J. Super. 424, 913 A.2d 166 (Ch. Div. 2006).*

Davis v. City of Plainfield, 913 A.2d 166 (N.J. Super. Ct. Ch. Div. 2006).

* In-state references to decisions appearing in New Jersey Reports or New Jersey Superior Court Reports should, where possible, include citations to those reports. With Superior Court decisions, the division of the court should be indicated: App. Div., Ch. Div. or Law Div.

New Mexico	
Coates v. Wal-Mart Stores, Inc., 1999-NMSC-013, 127 N.M. 47, 976 P.2d 999.*

Coates v. Wal-Mart Stores, Inc., 976 P.2d 999 (N.M. 1999).

Golden Oil Co. v. Chace Oil Co., 2000-NMCA-005, ¶ 16, 128 N.M. 526, 994 P.2d 772.*

Golden Oil Co. v. Chace Oil Co., 994 P.2d 772, 776 (N.M. Ct. App. 2000).

Gallegos v. Citizens Ins. Agency, 108 N.M. 722, 779 P.2d 99 (1989).*

Gallegos v. Citizens Ins. Agency, 779 P.2d 99 (N.M. 1989).

Buckingham v. Health S. Rehab. Hosp., 124 N.M. 419, 952 P.2d 20 (Ct. App. 1997).*

Buckingham v. Health S. Rehab. Hosp., 952 P.2d 20 (N.M. Ct. App. 1997).

Gallegos v. Yeargin W. Constructors, 104 N.M. 623, 725 P.2d 599 (Ct. App. 1986).*

Gallegos v. Yeargin W. Constructors, 725 P.2d 599 (N.M. Ct. App. 1986).

* In-state references to decisions appearing in New Mexico Reports should, where possible, include citations to those reports, in parallel with citations to the regional reporter. In addition in-state references to decisions from 1996 forward should include a medium-neutral citation which, under New Mexico rules, consists of the year, a court identifier, and a sequential decision number in the format shown here. Pinpoint cites should be to the paragraph numbers assigned by the court.

New York	
Anderson v. Rehab. Programs Found., 90 N.Y.2d 810, 688 N.E.2d 1381, 666 N.Y.S.2d 99 (1997).*

Anderson v. Rehab. Programs Found., 688 N.E.2d 1381 (N.Y. 1997).

Berkowitz v. Chavo Int'l Inc., 74 N.Y.2d 893, 547 N.E.2d 105, 547 N.Y.S.2d 850 (1989).*

Berkowitz v. Chavo Int'l Inc., 547 N.E.2d 105 (N.Y. 1989).

M.I.F. Sec. Co. v. R.C. Stamm & Co., 60 N.Y.2d 936, 459 N.E.2d 193, 471 N.Y.S.2d 84 (1983).*

M.I.F. Sec. Co. v. R.C. Stamm & Co., 459 N.E.2d 193 (N.Y. 1983).

Medici v. Dalton Sch., Inc., 34 N.Y.2d 735, 313 N.E.2d 789, 357 N.Y.S.2d 496 (1974).*

Medici v. Dalton Sch., Inc., 313 N.E.2d 789 (N.Y. 1974).

Schwartz v. Pub. Adm'r, 24 N.Y.2d 65, 246 N.E.2d 725, 298 N.Y.S.2d 955 (1968).*

Schwartz v. Pub. Adm'r, 246 N.E.2d 725 (N.Y. 1968).

Brown v. N.Y. City Econ. Dev. Corp., 234 A.D.2d 33, 650 N.Y.S.2d 213 (1st Dep't 1996).*

Brown v. N.Y. City Econ. Dev. Corp., 650 N.Y.S.2d 213 (N.Y. App. Div. 1996).

Hugo v. A & A Maint. Enter., 269 A.D.2d 357, 702 N.Y.S.2d 387 (2d Dep't 2000).*

Hugo v. A & A Maint. Enter., 702 N.Y.S.2d 387 (N.Y. App. Div. 2000).

Laro Maint. Corp. v. Culkin, 267 A.D.2d 431, 700 N.Y.S.2d 490 (2d Dep't 1999).*

Laro Maint. Corp. v. Culkin, 700 N.Y.S.2d 490 (N.Y. App. Div. 1999).

City of New York v. Park S. Assocs., 146 A.D.2d 537, 538 N.Y.S.2d 441 (1st Dep't 1989).*

City of New York v. Park S. Assocs., 538 N.Y.S.2d 441 (N.Y. App. Div. 1989).

IBM v. Universal Transcon. Corp., 191 A.D.2d 536, 595 N.Y.S.2d 106 (2d Dep't 1993).*

IBM v. Universal Transcon. Corp., 595 N.Y.S.2d 106 (N.Y. App. Div. 1993).

* In-state references to decisions appearing in New York Reports, Appellate Division Reports, or New York Miscellaneous Reports should, where possible, include citations to them. In addition, in-state references to decisions of the Supreme Court Appellate Division should normally indicate the Department.

North Carolina	
Chestnut v. Private Inv. Corp., 32 N.C. 363, 373 S.E.2d 542 (1988).*

Chestnut v. Private Inv. Corp., 373 S.E.2d 542 (N.C. 1988).

Nolan v. Forsyth Mem'l Hosp., 124 N.C. App. 670, 478 S.E.2d 676 (1996).*

Nolan v. Forsyth Mem'l Hosp., 478 S.E.2d 676 (N.C. Ct. App. 1996).

Joyner v. Town of Weaverville, 94 N.C. App. 588, 380 S.E.2d 536, (1989).*

Joyner v. Town of Weaverville, 380 S.E.2d 536, (N.C. Ct. App. 1989).

* In-state references to decisions appearing in North Carolina Reports or North Carolina Court of Appeals Reports should, where possible, include citations to them, in parallel with citations to the regional reporter.

North Dakota	
Linderkamp v. Hoffman, 1997 ND 64, ¶ 11, 562 N.W.2d 734.*

Linderkamp v. Hoffman, 562 N.W.2d 734, 737 (N.D. 1997).

Cont'l Res., Inc. v. Farrar Oil Co., 1997 ND 31, ¶ 12, 559 N.W.2d 841.*

Cont'l Res., Inc. v. Farrar Oil Co., 559 N.W.2d 841, 845 (N.D. 1997).

State v. Roberson, 1998 ND App 15, ¶ 12, 586 N.W.2d 687.*

State v. Roberson, 586 N.W.2d 687, 690 (N.D. Ct. App. 1998).

Norden Lab., Inc. v. Rotenberger, 358 N.W.2d 518 (N.D. 1984).

Dutchuk v. Bd. of Cnty. Comm'rs, 429 N.W.2d 21 (N.D. Ct. App. 1988).

* In-state references to decisions from 1997 forward should include a medium-neutral citation which, under North Dakota rules, consists of the year, a court identifier, and a sequential decision number in the format shown here. Pinpoint cites should be to the paragraph numbers assigned by the court.

Ohio	
Office of Disciplinary Counsel v. Shrode, 95 Ohio St. 3d 137, 2002-Ohio-1759, 766 N.E.2d 597, ¶ 8.*

Office of Disciplinary Counsel v. Shrode, 766 N.E.2d 597 (Ohio 2002).

Davis v. Columbus State Cmty. Coll. (1997), 78 Ohio St. 3d 1488, 678 N.E.2d 1227.*

Davis v. Columbus State Cmty. Coll., 678 N.E.2d 1227 (Ohio 1997).

Metro. Prop. & Liab. Ins. Co. v. Kott (1980), 62 Ohio St. 2d 114, 116, 403 N.E.2d 985.*

Metro. Prop. & Liab. Ins. Co. v. Kott, 403 N.E.2d 985, 986 (Ohio 1980).

Johnston v. Akron Ctr. for Reprod. Health, Inc. (1990), 68 Ohio App. 3d 655, 589 N.E.2d 432, motion overruled, 56 Ohio St. 3d 713, 565 N.E.2d 836.*

Johnston v. Akron Ctr. for Reprod. Health, Inc., 589 N.E.2d 432 (Ohio Ct. App.), motion overruled, 565 N.E.2d 836 (Ohio 1990).

* In-state references to decisions appearing in Ohio State Reports, Ohio Appellate Reports, or Ohio Miscellaneous Reports should, where possible, include citations to them. Ohio court practice is to place the year immediately following the parties' names rather than at the end of the citation. In addition, in-state references to decisions from 2002 forward should include a medium-neutral citation which, under Ohio rules, consists of the year, "Ohio", and a sequential decision number in the format shown in the first example. Pinpoint cites can be to the paragraph numbers assigned by the court reporter or, with pre-2002 decisions, to the official report alone.

Oklahoma	
Oliver v. Farmers Ins. of Cos., 1997 OK 71, ¶ 6, 941 P.2d 985.*

Oliver v. Farmers Ins. of Cos., 941 P.2d 985, 987 (Okla. 1997).

ABC Coating Co. v. J. Harris & Sons Ltd., 747 P.2d 271 (Okla. 1987).

Peacock v. State, 2002 OK CR 21, ¶ 5, 46 P.3d 713.*

Peacock v. State, 46 P.3d 713, 714 (Okla. Crim. App. 2002).

State ex rel. Gibson v. 1997 Dodge, 2001 OK CIV APP 130, ¶ 15, 35 P.3d 1009.*

State ex rel. Gibson v. 1997 Dodge, 35 P.3d 1009, 1013 (Okla. Civ. App. 2001).

* In-state references to decisions from 1997 forward should include a medium-neutral citation which, under Oklahoma rules, consists of the year, a court identifier, and a sequential decision number in the format shown here. Pinpoint cites should be to the paragraph numbers assigned by the court. Note that the Oklahoma Court of Criminal Appeals rather than the Oklahoma Supreme Court is the state's court of last resort in criminal matters.

Oregon	
Necanicum Inv. Co. v. Emp't Dep't, 345 Or 518, 200 P3d 129 (2008).*

Necanicum Inv. Co. v. Emp't Dep't, 200 P.3d 129 (Or. 2008).

Rocky B. Fisheries, Inc. v. N. Bend Fabrication & Mach., Inc., 297 Or 82, 679 P2d 1367 (1984).*

Rocky B. Fisheries, Inc. v. N. Bend Fabrication & Mach., Inc., 679 P.2d 1367 (Or. 1984).

Schilling v. SAIF Corp., 109 Or App 494, 820 P2d 471 (1991).*

Schilling v. SAIF Corp., 820 P.2d 471 (Or. Ct. App. 1991).

* In-state references to decisions appearing in Oregon Reports or Oregon Reports, Court of Appeals, should, where possible, include citations to them, abbreviated as illustrated above (omitting the periods called for by The Bluebook).

Pennsylvania	
Blakeney v. Green's Rest., 550 Pa. 689, 704 A.2d 1380 (1997).*

Blakeney v. Green's Rest., 704 A.2d 1380 (Pa. 1997).

Beckwith Mach. Co. v. Commonwealth, 485 Pa. 337, 402 A.2d 661 (1979).*

Beckwith Mach. Co. v. Commonwealth, 402 A.2d 661 (Pa. 1979).

Bullocks v. Aliquippa & S. R.R. Co., 364 Pa. Super. 642, 525 A.2d 812, appeal denied, 516 Pa. 621, 532 A.2d 19 (1987).*

Bullocks v. Aliquippa & S. R.R. Co., 525 A.2d 812 (Pa. Super. Ct.), appeal denied, 532 A.2d 19 (Pa. 1987).

Wells v. Cendant Mobility Fin. Corp., 2006 PA Super 363, ¶ 9, 913 A.2d 929, 933.*

Wells v. Cendant Mobility Fin. Corp., 913 A.2d 929, 933 (Pa. Super. Ct. 2006).

Weaver v. Pa. Bd. of Prob. & Parole, 688 A.2d 766 (Pa. Commw. Ct. 1997).

Keystone Outdoor Adver. v. Commonwealth, 687 A.2d 47 (Pa. Commw. Ct. 1996).

* In-state references to decisions appearing in Pennsylvania State Reports, Pennsylvania Superior Court Reports, or Pennsylvania Commonwealth Reports should, where possible, include citations to them, in parallel with citations to the regional reporter. The Pennsylvania Superior Court Reports ceased publication in 1998; the Pennsylvania Commonwealth Reports, in 1994. In addition, in-state references to decisions of the Superior Court should include a medium-neutral citation which consists of the year, a court identifier, and a sequential decision number in the format shown here. Pinpoint cites can be to the paragraph numbers assigned by that court.

Rhode Island	Brown & Sharp Mfg. Co. v. King, 404 A.2d 857 (R.I. 1979).
South Carolina	
Myrtle Beach Seafood Mkt., Inc. v. Rikard, 266 S.C. 52, 221 S.E.2d 399 (S.C. 1976).*

Myrtle Beach Seafood Mkt., Inc. v. Rikard, 221 S.E.2d 399 (S.C. 1976).

Carolina Chems., Inc. v. S.C. Dep't of Health & Envtl. Control, 290 S.C. 498, 351 S.E.2d 575 (Ct. App. 1986).*

Carolina Chems., Inc. v. S.C. Dep't of Health & Envtl. Control, 351 S.E.2d 575 (S.C. Ct. App. 1986).

* In-state references to decisions appearing in South Carolina Reports should, where possible, include citations to those reports, in parallel with citations to the regional reporter.

South Dakota	
Jansen v. Lemmon Fed. Credit Union, 1997 S.D. 44, ¶ 10, 562 N.W.2d 122, 125.*

Jansen v. Lemmon Fed. Credit Union, 562 N.W.2d 122, 125 (S.D. 1997).

Bohlmann v. Lindquist, 1997 S.D. 42, ¶ 13, 562 N.W.2d 578, 581.*

Bohlmann v. Lindquist, 562 N.W.2d 578, 581 (S.D. 1997).

Driscoll v. Great Plains Mktg. Co., 322 N.W.2d 478 (S.D. 1982).

* In-state references to decisions from 1996 forward should include a medium-neutral citation which, under current South Dakota rules, consists of the year, the state abbreviation (S.D.), and a sequential decision number in the format shown here. Pinpoint cites should include the paragraph numbers assigned by the court.

Tennessee	
Reagan v. Tenn. Mun. League, 751 S.W.2d 842 (Tenn. 1988).

Franklin Distrib. Co. v. Crush Int'l (U.S.A.), Inc., 726 S.W.2d 926 (Tenn. Ct. App. 1986).

Texas	
Mariner Fin. Grp., Inc. v. Bossley, 79 S.W.3d 30 (Tex. 2002).

Castaldo v. State, 78 S.W.3d 345 (Tex. Crim. App. 2002).

Birnbaum v. Alliance of Am. Insurers, 994 S.W.2d 766 (Tex. App.—Austin 1999, pet. denied).*

Birnbaum v. Alliance of Am. Insurers, 994 S.W.2d 766 (Tex. App. 1999).

Scoggins v. Best Indus. Unif. Supply Co., 899 S.W.2d 276 (Tex. App.—Houston [14th Dist.] 1995, no writ).*

Scoggins v. Best Indus. Unif. Supply Co., 899 S.W.2d 276 (Tex. App. 1995).

Walls Reg'l Hosp. v. Altaras, 903 S.W.2d 36 (Tex. App.—Waco 1994, orig. proceeding).*

Walls Reg'l Hosp. v. Altaras, 903 S.W.2d 36 (Tex. App. 1994).

* In-state references to decisions of the Texas Courts of Appeals should include a designation of the court plus an indication of any subsequent proceeding in the format shown.

Utah	
Utah Farm Bureau Ins. Co. v. Crook, 1999 UT 47, ¶ 6, 980 P.2d 685.*

Utah Farm Bureau Ins. Co. v. Crook, 980 P.2d 685, 686 (Utah 1999).

Fitz v. Synthes, 1999 UT 103, ¶ 11, 990 P.2d 391.*

Fitz v. Synthes, 990 P.2d 391, 393(Utah 1999).

Arrow Indus., Inc. v. Zions First Nat'l Bank, 767 P.2d 935 (Utah 1988).

* In-state references to decisions from 1999 forward should include a medium-neutral citation which, under Utah rules, consists of the year, the state postal abbreviation, and a sequential decision number in the format shown here. Pinpoint cites should be to the paragraph numbers assigned by the court.

Vermont	
Serecky v. Nat'l Grange Mut. Ins., 2004 VT 63, ¶ 15, 177 Vt. 58, 857 A.2d 775.*

Serecky v. Nat'l Grange Mut. Ins., 857 A.2d 775, 781 (Vt. 2005).

Ins. Co. of N. Am. v. Miller's Mut. Ins. Ass'n, 139 Vt. 255, 427 A.2d 354 (1981).*

Ins. Co. of N. Am. v. Miller's Mut. Ins. Ass'n, 427 A.2d 354 (Vt. 1981).

* In-state references to decisions appearing in Vermont Reports should, where possible, include citations to those reports, in parallel with citations to the regional reporter. In addition in-state references to decisions from 2003 forward should include a medium-neutral citation which, under Vermont rules, consists of the year, the state postal abbreviation, and a sequential decision number in the format shown here. Pinpoint cites should include the paragraph numbers assigned by the court. Vermont rules also call for the use of medium-neutral cites for cases from other jurisdictions that have adopted them.

Virginia	
Government Emps. Ins. Co. v. Moore, 266 Va. 155, 580 S.E.2d 823 (2003).*

Government Emps. Ins. Co. v. Moore, 580 S.E.2d 823 (Va. 2003).

Khanna v. Dominion Bank of N. Va., N.A., 237 Va. 242, 377 S.E.2d 378 (1989).*

Khanna v. Dominion Bank of N. Va., N.A., 377 S.E.2d 378 (Va. 1989).

First Fed. Sav. & Loan v. Gryder, 909 Va. App. 60, 383 S.E.2d 755 (1989).*

First Fed. Sav. & Loan v. Gryder, 383 S.E.2d 755 (Va. Ct. App. 1989).

* In-state references to decisions appearing in Virginia Reports or Virginia Court of Appeals Reports should, where possible, include citations to them, in parallel with citations to the regional reporter.

Washington	
State v. Heddrick, 166 Wn.2d 898, ¶ 20, 215 P.3d 201 (2009).*

State v. Heddrick, 215 P.3d 201, 206 (2009).

Shorewood W. Condo. Ass'n v. Sadri, 140 Wn.2d 47, 992 P.2d 1008 (2000).*

Shorewood W. Condo. Ass'n v. Sadri, 992 P.2d 1008 (Wash. 2000).

First United Methodist Church of Seattle v. Hearing Exam'r for Seattle Landmarks Pres. Bd., 129 Wn.2d 238, 916 P.2d 374 (1996).*

First United Methodist Church of Seattle v. Hearing Exam'r for Seattle Landmarks Pres. Bd., 916 P.2d 374 (Wash. 1996).

People's Org. for Wash. Energy Res. v. Utilities & Transp. Comm'n, 104 Wn.2d 798, 711 P.2d 319 (1985).*

People's Org. for Wash. Energy Res. v. Utilities & Transp. Comm'n, 711 P.2d 319 (Wash. 1985).

Cameron v. Murray , 151 Wn. App. 646, ¶ 14, 214 P.3d 150 (2009).*

Cameron v. Murray, 214 P.3d 150, 155 (2009).

Graves v. Vaagen Bros. Lumber, Inc., 55 Wn. App. 908, 781 P.2d 895 (1989).*

Graves v. Vaagen Bros. Lumber, Inc., 781 P.2d 895 (Wash. Ct. App. 1989).

* In-state references to decisions appearing in Washington Reports or Washington Appellate Reports should, where possible, include citations to them, abbreviated as illustrated above ("Wn." rather than The Bluebook's "Wash."), in parallel with citations to the regional reporter. Pinpoint cites need only use the page numbers in the official report or in the case of decisions issued since 2004 the paragraph numbers appearing in the official report.

West Virginia	
Syl. pt. 3, Cline v. Paramount Pac., Inc., 156 W. Va. 641, 196 S.E.2d 87 (1973).*

Cline v. Paramount Pac., Inc., 196 S.E.2d 87 (W. Va. 1973).

* In-state references to decisions appearing in West Virginia Reports should, where possible, include citations to those reports, in parallel with citations to the regional reporter. Case holdings should, were possible, be cited to syllabus points in the format illustrated.

Wisconsin	
Aicher v. Wis. Patients Comp., 2000 WI 98, ¶ 53, 237 Wis. 2d 99, 613 N.W.2d 849.*

Aicher v. Wis. Patients Comp., 613 N.W.2d 849, 865 (Wis. 2000).

Strasser v. Transtech Mobile Fleet Serv., Inc., 2000 WI 87, ¶ 60, 236 Wis. 2d 435, 613 N.W.2d 142.*

Strasser v. Transtech Mobile Fleet Serv., Inc., 613 N.W.2d 142, 155-56 (Wis. 2000).

Sudgen v. Bock, 2002 WI App 49, 251 Wis. 2d 344, 641 N.W.2d 693.*

Sudgen v. Bock, 641 N.W.2d 693 (Wis. Ct. App. 2002).

Blossom Farm Prods. Co. v. Kasson Cheese Co., 134 Wis. 2d 458, 401 N.W.2d 10 (1987).*

Blossom Farm Prods. Co. v. Kasson Cheese Co., 401 N.W.2d 10 (Wis. 1987).

Lipke v. Waushara Elec. Coop., 151 Wis. 2d 784, 447 N.W.2d 394 (Ct. App. 1989).*

Lipke v. Waushara Elec. Coop., 447 N.W.2d 394 (Wis. Ct. App. 1989).

* In-state references to decisions appearing in Wisconsin Reports should, where possible, include citations to those reports, in parallel with the regional reporter. In addition, in-state references to decisions from 2000 forward should include a medium-neutral citation which, under Wisconsin rules, consists of the year, a court identifier, and a sequential decision number in the format shown here. Pinpoint cites should be to the paragraph numbers assigned by the court.

Wyoming	
State v. Nelson, 2002 WY 99, ¶ 6, 49 P.3d 185 (Wyo. 2002).*

State v. Nelson, 49 P.3d 185, 188 (Wyo. 2002).

Wagner v. Wyo. Prod. Credit Ass'n, 773 P.2d 927 (Wyo. 1989).

* In-state references to decisions from 2001 forward should include a medium-neutral citation which, under Wyoming rules, consists of the year, the state postal abbreviation, and a sequential decision number in the format shown here. Pinpoint cites should be to the paragraph numbers assigned by the court. From January 1, 2004, forward the inclusion of a parallel cite is optional.


"""

if __name__ == '__main__':
    main(citationtxt_contents)
