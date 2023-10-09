#Use a 2d array to create a playlist system for 10 artists with 10 songs each. Your algorithm will create a random order for the songs, with the bands having a minimum distance of 2 songs. i.e. you can't play the same band again until 2 songs have passed. (You do not have to play EVERY song in the system, just 20 is enough.)
import random
playlist = [['Led Zeppelin', 'Stairway to Heaven', 'Kashmir', 'Whole Lotta Love', 'Black Dog', 'Rock and Roll', 'When the Levee Breaks', 'Immigrant Song', 'Dazed and Confused', 'Ramble On', 'Good Times Bad Times'],['The Beatles', 'Hey Jude', 'Let It Be', 'A Hard Day\'s Night', 'Help!', 'Twist and Shout', 'Come Together', 'Something', 'Yesterday', 'All You Need Is Love', 'I Want to Hold Your Hand'],['Pink Floyd', 'Comfortably Numb', 'Wish You Were Here', 'Another Brick in the Wall', 'Time', 'Money', 'Shine On You Crazy Diamond', 'Us and Them', 'Brain Damage', 'Eclipse', 'The Great Gig in the Sky'],['Black Sabbath', 'Paranoid', 'Iron Man', 'War Pigs', 'N.I.B.', 'Sabbath Bloody Sabbath', 'Children of the Grave', 'Sweet Leaf', 'Fairies Wear Boots', 'Snowblind', 'Into the Void'],['Rush', 'Tom Sawyer', 'The Spirit of Radio', 'Limelight', 'YYZ', 'Closer to the Heart', 'Red Barchetta', 'Freewill', 'Working Man', 'Subdivisions', 'Fly by Night'],['Oasis', 'Wonderwall', 'Don\'t Look Back in Anger', 'Champagne Supernova', 'Live Forever', 'Some Might Say', 'Morning Glory', 'Slide Away', 'Cigarettes & Alcohol', 'Supersonic', 'The Masterplan'],['The Who', 'Baba O\'Riley', 'Won\'t Get Fooled Again', 'My Generation', 'Pinball Wizard', 'Behind Blue Eyes', 'I Can See for Miles', 'Substitute', 'The Kids Are Alright', 'Love Reign O\'er Me', 'Squeeze Box'],['Jeff Beck', 'Cause We\'ve Ended as Lovers', 'Freeway Jam', 'Beck\'s Bolero', 'Brush with the Blues', 'Goodbye Pork Pie Hat', 'Blue Wind', 'Led Boots', 'Scatterbrain', 'People Get Ready', 'You Know What I Mean'],['King Crimson', '21st Century Schizoid Man', 'In the Court of the Crimson King', 'Epitaph', 'Starless', 'Red', 'Larks\' Tongues in Aspic Part I', 'The Night Watch', 'Frame by Frame', 'Discipline', 'Elephant Talk'],['Metallica', 'Enter Sandman', 'Master of Puppets', 'One', 'Nothing Else Matters', 'The Unforgiven', 'For Whom the Bell Tolls', 'Fade to Black', 'Seek and Destroy', 'Battery', 'Creeping Death']]
song_count = 0
distance_count = [0]*10
played_yet = [False]*10
for x in range(0,20):
  band = random.randrange(0,10)
  if played_yet[band] != False:
    if distance_count[band] >= 2:
      song = random.randrange(1,10)
      print(playlist[band][0]+":", playlist[band][song])
    else:
      while distance_count[band] <= 2:
        band = random.randrange(0,10)
      song = random.randrange(1,10)
      print(playlist[band][0]+":", playlist[band][song])
  else:
    song = random.randrange(1,10)
    print(playlist[band][0]+":", playlist[band][song])
  for y in range(len(distance_count)):
    if y != band:
      distance_count[y] += 1
    else:
      distance_count[y] = 0
      played_yet[y] = True
  band = ''
  song = ''
