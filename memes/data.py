import pymysql

# Replace with your actual MySQL database connection details
connection = pymysql.connect(
    host="localhost",
    user="root",
    password="Manasi@123",
    database="meme_viewer"
)

cursor = connection.cursor()

# Sample data to insert
data_to_insert = [
    ('Meme 1',
     'https://www.happierhuman.com/wp-content/uploads/2022/01/memes-about-life-sayingimages-im-fine-totally-fine-min.jpg'),
    ('Meme 2',
     'https://www.happierhuman.com/wp-content/uploads/2022/01/memes-about-life-sayingimages-congrats-guys-min.jpg'),
    ('Meme 3',
     'https://www.happierhuman.com/wp-content/uploads/2022/01/memes-about-life-sayingimages-im-used-to-it-anyway-min.jpg'),
    ('meme 4',
     'https://cdn4.sharechat.com/BTSFunnyMemes_14ed89a6_1632303505626_sc_cmprsd_40.jpg?tenant=sc&referrer=pwa-sharechat-service&f=rsd_40.jpg'),
    ('meme 5',
     'https://i.pinimg.com/736x/29/1a/58/291a58216476c6b73d05ec70e097ac48.jpg'),
    ('meme 6',
     'https://www.happierhuman.com/wp-content/uploads/2022/04/funny-memes-work-stress-fairygoodboss-designated-crying-area-768x780.jpg'),
    ('meme 7',
     'https://www.happierhuman.com/wp-content/uploads/2022/04/funny-memes-work-stress-fairygodboss-why-am-i-not-rich-yet.jpg'),
    ('meme 8',
     'https://www.happierhuman.com/wp-content/uploads/2022/04/funny-memes-work-stress-fairygodboss-my-actual-face-every-morning.jpg'),
    ('meme 9',
     'https://www.happierhuman.com/wp-content/uploads/2022/04/funny-memes-work-stress-fairygodboss-story-of-my-life.jpg'),
    ('meme 10',
     'https://www.happierhuman.com/wp-content/uploads/2022/04/funny-memes-work-stress-fairygodboss-should-i-just-leave-768x741.png'),
    ('meme 11',
     'https://www.weareteachers.com/wp-content/uploads/after-sub-meme.png'),
    ('meme 12',
     'https://www.weareteachers.com/wp-content/uploads/cold-classroom-meme.png'),
    ('meme 13', 'https://www.weareteachers.com/wp-content/uploads/first-snowflake-school-meme.png'),
    ('meme 14', 'https://www.weareteachers.com/wp-content/uploads/hearding-cats-meme.png'),
    ('meme 15', 'https://www.weareteachers.com/wp-content/uploads/live-at-school-meme.png'),
    ('meme 16', 'https://www.weareteachers.com/wp-content/uploads/nameless-paper-meme.png'),
    ('meme 17', 'https://www.happierhuman.com/wp-content/uploads/2022/04/funny-memes-work-stress-fairygodboss-yeah-right.jpg'),
    ('meme 18', 'https://www.happierhuman.com/wp-content/uploads/2022/04/funny-memes-work-stress-fairygodboss-how-about-i-just-leave-for-good.jpg'),
    ('meme 19', 'https://i.pinimg.com/1200x/d5/f3/92/d5f392502fab2cc33322574faf54a1ec.jpg'),
    ('meme 20', 'https://i.pinimg.com/564x/65/da/97/65da9762f204e689aee27e4daf3fde25.jpg'),
    ('meme 21', 'https://i.pinimg.com/564x/a1/72/e2/a172e2c2f09193caf9ac49fbd20adfe1.jpg'),
    ('meme 22', 'https://i.pinimg.com/564x/49/49/41/4949411514599cc072a22e5d334baa46.jpg'),
    ('meme 23', 'https://blog.creativesafetysupply.com/wp-content/uploads/2012/10/engmeme1-e1522631559599.png'),
    ('meme 24', 'https://blog.creativesafetysupply.com/wp-content/uploads/2012/10/engmeme2.png'),
    ('meme 25', 'https://blog.creativesafetysupply.com/wp-content/uploads/2012/10/engmeme3-e1522631793956.png'),
    ('meme 26', 'https://blog.creativesafetysupply.com/wp-content/uploads/2012/10/engmeme5-e1522631934225.png'),
    ('meme 27', 'https://i.pinimg.com/564x/5a/0a/6c/5a0a6c3792945c364dac422106109485.jpg'),
    ('meme 28', 'https://i.pinimg.com/564x/b5/e7/12/b5e712718b511a008f51ca8bd0f48356.jpg'),
    ('meme 29', 'https://i.pinimg.com/564x/07/61/08/076108743dc361a583c94331475d8458.jpg'),
    ('meme 30', 'https://i.pinimg.com/564x/57/c5/62/57c5621d8d599020e673e531251517ef.jpg'),
    ('meme 31', 'https://i.pinimg.com/564x/35/5f/b5/355fb544dabc14e2377f0e9fa5f9dd6b.jpg'),
    ('meme 32', 'https://i.pinimg.com/564x/9d/ad/1e/9dad1e895e3998f113be295c8dbbba17.jpg'),
    ('meme 33', 'https://i.pinimg.com/564x/ce/36/a9/ce36a9e5e7b837b002ef390c57b47f4a.jpg'),
    ('meme 34', 'https://i.pinimg.com/564x/56/88/7c/56887c0968077a5fbeaa176d06bb5dd1.jpg'),
    ('meme 35', 'https://i.pinimg.com/564x/35/d5/f0/35d5f089d60ba23275ccbbd27378fc2d.jpg'),
    ('meme 36', 'https://i.pinimg.com/564x/98/30/d4/9830d48bce2235ab312f84b4938c0949.jpg'),
    ('meme 37', 'https://i.pinimg.com/564x/be/f1/80/bef180586aab52a89a1e4095ec5dd8cc.jpg'),
    ('meme 38', 'https://i.pinimg.com/564x/c5/e9/f3/c5e9f3934ede49b11bf502edc392e68a.jpg'),
    ('meme 39', 'https://i.pinimg.com/564x/98/9c/0d/989c0dac52fbddb2fd8bbe0b51b2db21.jpg'),
    ('meme 40', 'https://i.pinimg.com/736x/45/2b/c0/452bc0866908a7bb84beb6897c020e80.jpg'),
    ('meme 41', 'https://i.pinimg.com/564x/9e/7f/67/9e7f670325c46afee9b1552e2a9be841.jpg'),
    ('meme 42', 'https://i.pinimg.com/564x/96/7a/8d/967a8d89d829270bd77be805d54bfe89.jpg'),
    ('meme 43', 'https://i.pinimg.com/564x/c7/e6/22/c7e622d453cd13be484f999e35937435.jpg'),
    ('meme 44', 'https://i.pinimg.com/564x/ef/ca/29/efca293a52a8692d4c2120cfb2374618.jpg'),
    ('meme 45', 'https://i.pinimg.com/564x/30/b1/12/30b1121076746c604a96023198f51bc4.jpg'),
    ('meme 46', 'https://i.pinimg.com/564x/48/d7/b1/48d7b1666d764e17fd37237343c8be05.jpg'),
    ('meme 47', 'https://i.pinimg.com/564x/82/4c/2e/824c2ecaeda08eddb06b6b40af93ed1c.jpg'),
    ('meme 48', 'https://i.pinimg.com/564x/8c/80/65/8c8065f3b46b0c795280c8329f4499d8.jpg'),
    ('meme 49', 'https://i.pinimg.com/564x/07/06/bb/0706bbcb35e6e17ff0c11c75ec83b148.jpg'),
    ('meme 50', 'https://i.pinimg.com/564x/d1/60/1a/d1601a67e93e9c8063878a57dbbbd651.jpg'),

]

# Insert data into the memes table
for meme_data in data_to_insert:
    cursor.execute("INSERT INTO memes (name, image_url) VALUES (%s, %s)", meme_data)

# Commit the changes
connection.commit()

# Close the cursor and connection
cursor.close()
connection.close()
