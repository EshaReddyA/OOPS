import sqlite3

# Connect to database (creates file if it doesn't exist)
conn = sqlite3.connect("school.db")
cursor = conn.cursor()

# Create a table
cursor.execute('''
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    surname TEXT NOT NULL,
    name TEXT NOT NULL,
    address TEXT,
    roll_no INTEGER UNIQUE NOT NULL,
    section TEXT
)
''')
# cursor.execute(
#     "INSERT INTO students (id, surname, name, address, roll_no, section) VALUES (?,?, ?, ?, ?, ?)",
#     (1,"Doe", "John", "123 Main St", 101, "A")
# )
# cursor.execute("INSERT INTO students (id, surname, name, address, roll_no, section) VALUES (2, 'Johnson', 'Melanie', '109 Julie Ridge, Lake Daniel, WA 45591', 126, 'A')")
# cursor.execute("INSERT INTO students (id, surname, name, address, roll_no, section) VALUES (3, 'Young', 'Benjamin', '080 Kristin Falls Apt. 629, West Michael, OK 50876', 150, 'C')")
# cursor.execute("INSERT INTO students (id, surname, name, address, roll_no, section) VALUES (4, 'Thompson', 'Elizabeth', '59191 White Station, New Rodney, MD 74999', 104, 'A')")
# cursor.execute("INSERT INTO students (id, surname, name, address, roll_no, section) VALUES (5, 'Williams', 'Gregory', 'Unit 8161 Box 2778, DPO AP 87625', 107, 'A')")
# cursor.execute("INSERT INTO students (id, surname, name, address, roll_no, section) VALUES (6, 'Hill', 'Tiffany', '82679 Patricia Gateway, Port Tina, MA 22061', 136, 'D')")
# cursor.execute("INSERT INTO students (id, surname, name, address, roll_no, section) VALUES (7, 'Gonzalez', 'Luis', 'USS Torres, FPO AA 07313', 137, 'D')")
# cursor.execute("INSERT INTO students (id, surname, name, address, roll_no, section) VALUES (8, 'Cox', 'Henry', '4698 Teresa Freeway, Davidton, WI 47863', 133, 'A')")
# cursor.execute("INSERT INTO students (id, surname, name, address, roll_no, section) VALUES (9, 'Larson', 'Lisa', '88287 Gibson Plains Suite 140, South Tammy, MD 81984', 196, 'D')")
# cursor.execute("INSERT INTO students (id, surname, name, address, roll_no, section) VALUES (10, 'Chan', 'Sarah', '713 Marshall Plaza Apt. 333, Port Virginia, VT 59317', 146, 'D')")
# cursor.execute("INSERT INTO students (id, surname, name, address, roll_no, section) VALUES (11, 'Perez', 'Carmen', '37666 Andrew Well Suite 308, South Ashley, WA 19314', 187, 'A')")
# cursor.execute("INSERT INTO students (id, surname, name, address, roll_no, section) VALUES (12, 'Martinez', 'Michael', '38330 Michael Station, North Alexishaven, VA 78845', 142, 'A')")
# cursor.execute("INSERT INTO students (id, surname, name, address, roll_no, section) VALUES (13, 'Werner', 'Troy', '74608 John Flats Apt. 109, Pinedaview, CO 23684', 109, 'D')")
# cursor.execute("INSERT INTO students (id, surname, name, address, roll_no, section) VALUES (14, 'Brown', 'Andrew', '63193 Michael Loop Apt. 517, West Vanessachester, NM 82642', 180, 'D')")
# cursor.execute("INSERT INTO students (id, surname, name, address, roll_no, section) VALUES (15, 'Ross', 'Phillip', 'USNS Martinez, FPO AA 06478', 175, 'B')")
# cursor.execute("INSERT INTO students (id, surname, name, address, roll_no, section) VALUES (16, 'Koch', 'Jared', '49836 Taylor Lodge Suite 185, West Kelseyburgh, LA 03768', 138, 'C')")
# cursor.execute("INSERT INTO students (id, surname, name, address, roll_no, section) VALUES (17, 'Roberts', 'Christina', 'Unit 6697 Box 2454, DPO AP 43990', 182, 'A')")
# cursor.execute("INSERT INTO students (id, surname, name, address, roll_no, section) VALUES (18, 'Randall', 'Beth', '0389 Walker Neck Suite 026, North Erin, AR 17370', 157, 'B')")
# cursor.execute("INSERT INTO students (id, surname, name, address, roll_no, section) VALUES (19, 'Parker', 'Jeffery', '7262 Philip Trafficway, Bruceton, PA 45171', 170, 'B')")
# cursor.execute("INSERT INTO students (id, surname, name, address, roll_no, section) VALUES (20, 'Miller', 'Alan', '52170 Dawn Way Suite 820, Lake Lisaborough, AK 90998', 108, 'C')")
# cursor.execute("INSERT INTO students (id, surname, name, address, roll_no, section) VALUES (21, 'Smith', 'Sophia', '2954 Gilbert View Suite 808, South Mary, VA 58681', 105, 'D')")
# cursor.execute("INSERT INTO students (id, surname, name, address, roll_no, section) VALUES (22, 'Crosby', 'Sarah', '3171 Nicholas Loaf, New Harold, AK 44877', 153, 'A')")
# cursor.execute("INSERT INTO students (id, surname, name, address, roll_no, section) VALUES (23, 'Obrien', 'Joshua', '96735 Hill Mountains Suite 914, Nicholstown, PA 03007', 120, 'B')")
# cursor.execute("INSERT INTO students (id, surname, name, address, roll_no, section) VALUES (24, 'Greer', 'Ashley', '995 Vanessa Shoals Apt. 563, Tuckerview, CT 41292', 164, 'B')")
# cursor.execute("INSERT INTO students (id, surname, name, address, roll_no, section) VALUES (25, 'Wallace', 'Melissa', '920 Huerta Heights Apt. 274, Port Austinbury, GA 21642', 119, 'C')")
# cursor.execute("INSERT INTO students (id, surname, name, address, roll_no, section) VALUES (26, 'Faulkner', 'Elizabeth', 'Unit 3667 Box 0573, DPO AA 12151', 124, 'A')")
# cursor.execute("INSERT INTO students (id, surname, name, address, roll_no, section) VALUES (27, 'Hernandez', 'Derek', 'PSC 4156, Box 8920, APO AE 07907', 122, 'A')")
# cursor.execute("INSERT INTO students (id, surname, name, address, roll_no, section) VALUES (28, 'Cantu', 'Steven', '781 Dakota Grove Suite 097, West Kristenborough, SD 05445', 181, 'C')")
# cursor.execute("INSERT INTO students (id, surname, name, address, roll_no, section) VALUES (29, 'Anderson', 'Stephanie', '39218 Holland Causeway, West Holly, AK 88834', 171, 'D')")
# cursor.execute("INSERT INTO students (id, surname, name, address, roll_no, section) VALUES (30, 'Banks', 'Christina', '4128 Baker Valley Suite 206, Matthewberg, IL 61555', 132, 'A')")
# cursor.execute("INSERT INTO students (id, surname, name, address, roll_no, section) VALUES (31, 'Daniels', 'Casey', '1233 Dean Plain Apt. 888, Bradleyshire, TN 08339', 134, 'D')")
# cursor.execute("INSERT INTO students (id, surname, name, address, roll_no, section) VALUES (32, 'Gonzalez', 'Patricia', '223 George Haven, Campbellville, DC 49296', 156, 'D')")
# cursor.execute("INSERT INTO students (id, surname, name, address, roll_no, section) VALUES (33, 'Moreno', 'Tracy', '584 Jeremy Terrace, Chasehaven, MT 59315', 143, 'B')")
# cursor.execute("INSERT INTO students (id, surname, name, address, roll_no, section) VALUES (34, 'Kaiser', 'Brandon', '44763 Johnson Springs Suite 123, Braymouth, LA 39508', 169, 'A')")
# cursor.execute("INSERT INTO students (id, surname, name, address, roll_no, section) VALUES (35, 'Hancock', 'Karen', '5288 Candace Drive Suite 572, New Richardborough, AL 51038', 125, 'C')")
# cursor.execute("INSERT INTO students (id, surname, name, address, roll_no, section) VALUES (36, 'Peters', 'Rebecca', '51397 Morse Courts Apt. 034, Andrewsfort, ME 22797', 162, 'D')")
# cursor.execute("INSERT INTO students (id, surname, name, address, roll_no, section) VALUES (37, 'Young', 'Tammy', '46448 Stephen Burgs Suite 291, Lake Timothy, OR 47183', 144, 'B')")
# cursor.execute("INSERT INTO students (id, surname, name, address, roll_no, section) VALUES (38, 'Brown', 'Adam', '5604 Wolfe Light Apt. 579, Gaineston, KY 45042', 148, 'D')")
# cursor.execute("INSERT INTO students (id, surname, name, address, roll_no, section) VALUES (39, 'Walker', 'Anthony', '442 Lorraine Extensions, North Christybury, AZ 16868', 167, 'C')")
# cursor.execute("INSERT INTO students (id, surname, name, address, roll_no, section) VALUES (40, 'Moore', 'Michael', '097 Robin Springs, New Mario, CO 81502', 152, 'B')")
# cursor.execute("INSERT INTO students (id, surname, name, address, roll_no, section) VALUES (41, 'Pacheco', 'Donna', '421 Adams Loaf, Staceytown, MI 83503', 128, 'A')")
# cursor.execute("INSERT INTO students (id, surname, name, address, roll_no, section) VALUES (42, 'Thompson', 'Mackenzie', '730 Maldonado Heights, Christinefurt, VT 88765', 118, 'C')")
# cursor.execute("INSERT INTO students (id, surname, name, address, roll_no, section) VALUES (43, 'Meyer', 'Amber', '02159 Scott Inlet Suite 294, New Kurt, AL 93573', 186, 'A')")
# cursor.execute("INSERT INTO students (id, surname, name, address, roll_no, section) VALUES (44, 'Baxter', 'Justin', '850 Charles Spring Suite 633, South Karina, WI 93589', 160, 'B')")
# cursor.execute("INSERT INTO students (id, surname, name, address, roll_no, section) VALUES (45, 'Griffin', 'Jason', '056 Villegas Row Apt. 427, Lake Nicholasbury, NH 48069', 199, 'C')")
# cursor.execute("INSERT INTO students (id, surname, name, address, roll_no, section) VALUES (46, 'Nelson', 'James', '4533 Joyce Roads, East Kent, ND 27534', 163, 'C')")
# cursor.execute("INSERT INTO students (id, surname, name, address, roll_no, section) VALUES (47, 'Watkins', 'Kristen', 'USNV Sullivan, FPO AE 99138', 184, 'B')")
# cursor.execute("INSERT INTO students (id, surname, name, address, roll_no, section) VALUES (48, 'Perez', 'Charles', '932 Jennifer Crossroad, Port Jessicamouth, MO 51009', 190, 'D')")
# cursor.execute("INSERT INTO students (id, surname, name, address, roll_no, section) VALUES (49, 'Townsend', 'Kimberly', '000 Stacy Rue Suite 069, Smithville, GA 26658', 194, 'A')")
# cursor.execute("INSERT INTO students (id, surname, name, address, roll_no, section) VALUES (50, 'Bryant', 'Brooke', '13555 Brown Knolls Apt. 518, West Saramouth, TN 96129', 200, 'C')")
# cursor.execute("INSERT INTO students (id, surname, name, address, roll_no, section) VALUES (51, 'Lawson', 'Anthony', '861 Clark Orchard, West Michelle, SD 09042', 106, 'C')")
# cursor.execute("INSERT INTO students (id, surname, name, address, roll_no, section) VALUES (52, 'Harris', 'Brittany', '829 Suarez Manors Suite 237, New Michael, ME 41156', 161, 'D')")
# cursor.execute("INSERT INTO students (id, surname, name, address, roll_no, section) VALUES (53, 'Foster', 'Thomas', '4913 Thomas Plains, Christopherport, TN 90548', 140, 'D')")
# cursor.execute("INSERT INTO students (id, surname, name, address, roll_no, section) VALUES (54, 'Snyder', 'Jason', '16393 Navarro Estate, Port Coryborough, SC 40709', 192, 'A')")
# cursor.execute("INSERT INTO students (id, surname, name, address, roll_no, section) VALUES (55, 'Pitts', 'James', '2955 Moore Expressway Apt. 905, Donnaland, OH 93116', 117, 'D')")
# cursor.execute("INSERT INTO students (id, surname, name, address, roll_no, section) VALUES (56, 'Mullen', 'Michaela', '7005 Knight Ferry Apt. 775, Port Cody, ID 79952', 185, 'D')")
# cursor.execute("INSERT INTO students (id, surname, name, address, roll_no, section) VALUES (57, 'Lopez', 'Alexandria', '30358 Gloria Fort Suite 199, West Jerrystad, AL 39786', 154, 'C')")
# cursor.execute("INSERT INTO students (id, surname, name, address, roll_no, section) VALUES (58, 'Nicholson', 'Misty', '3828 Byrd Springs, New Christopherchester, SC 63206', 112, 'D')")
# cursor.execute("INSERT INTO students (id, surname, name, address, roll_no, section) VALUES (59, 'Lewis', 'Anthony', '7968 Heidi Fort Apt. 014, Sanchezmouth, ID 44365', 197, 'C')")
# cursor.execute("INSERT INTO students (id, surname, name, address, roll_no, section) VALUES (60, 'Downs', 'John', '96756 Ashley Groves Suite 945, North Susanborough, AZ 30512', 177, 'A')")
# cursor.execute("INSERT INTO students (id, surname, name, address, roll_no, section) VALUES (61, 'Summers', 'Hannah', '024 Mason Greens, Josephstad, PA 57915', 116, 'B')")
# cursor.execute("INSERT INTO students (id, surname, name, address, roll_no, section) VALUES (62, 'Frazier', 'Ashley', '73089 John Alley Apt. 997, Butlerborough, MA 40170', 174, 'B')")
# cursor.execute("INSERT INTO students (id, surname, name, address, roll_no, section) VALUES (63, 'Benson', 'Amy', '92894 Virginia Pines, Markchester, ME 72778', 189, 'C')")
# cursor.execute("INSERT INTO students (id, surname, name, address, roll_no, section) VALUES (64, 'Webb', 'Melanie', '1267 Christopher Landing, North Tonifurt, AK 63490', 172, 'D')")
# cursor.execute("INSERT INTO students (id, surname, name, address, roll_no, section) VALUES (65, 'Gibbs', 'Matthew', '830 Reynolds Island, Port Tonyafurt, TN 09328', 173, 'C')")
# cursor.execute("INSERT INTO students (id, surname, name, address, roll_no, section) VALUES (66, 'Brown', 'Gail', '12825 Jennifer Flats, Lake Jacquelinestad, SD 53635', 141, 'D')")
# cursor.execute("INSERT INTO students (id, surname, name, address, roll_no, section) VALUES (67, 'Freeman', 'Monica', '9873 Cardenas River, Smithside, WV 39705', 114, 'A')")
# cursor.execute("INSERT INTO students (id, surname, name, address, roll_no, section) VALUES (68, 'Salazar', 'Linda', '5211 Smith Freeway, New Jacqueline, NH 82694', 178, 'B')")
# cursor.execute("INSERT INTO students (id, surname, name, address, roll_no, section) VALUES (69, 'Gibbs', 'Vickie', '311 Warren Meadow Apt. 690, Andrewfort, DE 59826', 121, 'C')")
# cursor.execute("INSERT INTO students (id, surname, name, address, roll_no, section) VALUES (70, 'Wilkinson', 'Stephanie', '52320 Oscar Divide Apt. 703, Codyhaven, NV 94007', 151, 'B')")
# cursor.execute("INSERT INTO students (id, surname, name, address, roll_no, section) VALUES (71, 'Cox', 'Cesar', 'Unit 0433 Box 8554, DPO AP 97039', 102, 'A')")
# cursor.execute("INSERT INTO students (id, surname, name, address, roll_no, section) VALUES (72, 'Martinez', 'Michelle', '469 Cain Harbor Apt. 201, Woodville, WY 09692', 176, 'D')")
# cursor.execute("INSERT INTO students (id, surname, name, address, roll_no, section) VALUES (73, 'Newman', 'Lisa', '003 Adkins Station Apt. 258, North Jamesview, OH 34590', 103, 'D')")
# cursor.execute("INSERT INTO students (id, surname, name, address, roll_no, section) VALUES (74, 'Friedman', 'Michelle', '82427 Morris Prairie, Jamesstad, VA 41280', 111, 'D')")
# cursor.execute("INSERT INTO students (id, surname, name, address, roll_no, section) VALUES (75, 'Ramirez', 'Carla', '50857 George Club, New Brandonmouth, MT 13969', 158, 'D')")
# cursor.execute("INSERT INTO students (id, surname, name, address, roll_no, section) VALUES (76, 'Ferguson', 'Harold', '8853 Tina Mills, Vanessatown, KS 17336', 191, 'B')")
# cursor.execute("INSERT INTO students (id, surname, name, address, roll_no, section) VALUES (77, 'Everett', 'Michelle', '361 Vega Union, Walkerfurt, OH 56057', 145, 'A')")
# cursor.execute("INSERT INTO students (id, surname, name, address, roll_no, section) VALUES (78, 'Brown', 'Seth', '1873 Wood Pike, Lake Carolineberg, HI 32236', 149, 'B')")
# cursor.execute("INSERT INTO students (id, surname, name, address, roll_no, section) VALUES (79, 'Daugherty', 'Pamela', '60146 Timothy Parks Apt. 516, South Cody, MT 15263', 113, 'B')")
# cursor.execute("INSERT INTO students (id, surname, name, address, roll_no, section) VALUES (80, 'Clark', 'Christopher', 'PSC 8704, Box 8088, APO AA 36536', 198, 'C')")
# cursor.execute("INSERT INTO students (id, surname, name, address, roll_no, section) VALUES (81, 'Ross', 'Craig', 'USNV Mitchell, FPO AP 98636', 188, 'A')")
# cursor.execute("INSERT INTO students (id, surname, name, address, roll_no, section) VALUES (82, 'Murphy', 'Paul', '683 Anderson Greens Apt. 555, Dawnfurt, HI 32817', 166, 'D')")
# cursor.execute("INSERT INTO students (id, surname, name, address, roll_no, section) VALUES (83, 'Miller', 'Susan', '17833 Louis Gardens, Cortezbury, MD 39641', 159, 'B')")
# cursor.execute("INSERT INTO students (id, surname, name, address, roll_no, section) VALUES (84, 'Patterson', 'Tiffany', '7844 Alexander Union Apt. 030, New Amandaside, IL 39381', 193, 'B')")
# cursor.execute("INSERT INTO students (id, surname, name, address, roll_no, section) VALUES (85, 'Wilson', 'Wesley', '847 Thomas Forges Suite 843, Johnton, IA 39995', 131, 'D')")
# cursor.execute("INSERT INTO students (id, surname, name, address, roll_no, section) VALUES (86, 'Carter', 'Colton', '98946 Bradford Greens, New Nathan, IA 32402', 168, 'D')")
# cursor.execute("INSERT INTO students (id, surname, name, address, roll_no, section) VALUES (87, 'Goodman', 'Adam', '0419 John Mission, Thomasville, ID 48377', 130, 'C')")
# cursor.execute("INSERT INTO students (id, surname, name, address, roll_no, section) VALUES (88, 'Navarro', 'Brian', '524 Christopher Street Suite 148, North Markmouth, MO 77930', 129, 'C')")
# cursor.execute("INSERT INTO students (id, surname, name, address, roll_no, section) VALUES (89, 'Price', 'Katherine', '781 Mcintyre Turnpike, New Anita, OR 10838', 165, 'C')")
# cursor.execute("INSERT INTO students (id, surname, name, address, roll_no, section) VALUES (90, 'Wood', 'Daniel', '66310 Rogers Ridge Apt. 639, Frederickfort, MO 43367', 195, 'A')")
# cursor.execute("INSERT INTO students (id, surname, name, address, roll_no, section) VALUES (91, 'Park', 'Veronica', '1155 Jennifer Station Apt. 840, Robertsview, LA 10443', 179, 'C')")
# cursor.execute("INSERT INTO students (id, surname, name, address, roll_no, section) VALUES (92, 'Rodriguez', 'Michael', '07910 Kathleen Inlet, Lake Peter, SD 81632', 135, 'D')")
# cursor.execute("INSERT INTO students (id, surname, name, address, roll_no, section) VALUES (93, 'Powell', 'Denise', 'PSC 6966, Box 4222, APO AP 79887', 127, 'A')")
# cursor.execute("INSERT INTO students (id, surname, name, address, roll_no, section) VALUES (94, 'Smith', 'Jose', '07238 Patel Cliffs Apt. 219, Rebeccaborough, IN 90141', 139, 'A')")
# cursor.execute("INSERT INTO students (id, surname, name, address, roll_no, section) VALUES (95, 'Graves', 'Carolyn', 'PSC 7206, Box 9116, APO AE 69005', 110, 'D')")
# cursor.execute("INSERT INTO students (id, surname, name, address, roll_no, section) VALUES (96, 'Walker', 'Duane', '810 Chapman Stravenue Apt. 828, North Tiffanytown, VA 64553', 115, 'C')")
# cursor.execute("INSERT INTO students (id, surname, name, address, roll_no, section) VALUES (97, 'Wolfe', 'Ryan', '3049 Koch Walk Apt. 827, East Sandraborough, KS 24777', 123, 'D')")
# cursor.execute("INSERT INTO students (id, surname, name, address, roll_no, section) VALUES (98, 'Mills', 'Christian', '15101 Long Prairie, Christensenland, WI 04654', 183, 'C')")
# cursor.execute("INSERT INTO students (id, surname, name, address, roll_no, section) VALUES (99, 'Morales', 'Kayla', '4588 Heidi Fort Suite 771, Braunborough, WY 66297', 147, 'C')")
# cursor.execute("INSERT INTO students (id, surname, name, address, roll_no, section) VALUES (100, 'Ray', 'Kathleen', 'PSC 8420, Box 2697, APO AP 19596', 155, 'A')")
# conn.commit()
# cursor.execute("SELECT * FROM students")
# for row in cursor:
#     print(row) 
    
# cursor.execute("UPDATE students SET address = '999 New St, NY' WHERE id = 5")
#cursor.execute("DELETE FROM students WHERE roll_no = ?", (183,))
conn.commit()
conn.close()
