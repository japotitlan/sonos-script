# Import soco and get a SoCo instance
import soco
device = soco.discovery.any_soco()

nombre = device.player_name
ip = device.ip_address

print(nombre)
print(ip)

device.volume = 40
# Get all albums from the music library that contains the word "Black"
# and add them to the queue
albums = device.music_library.get_albums(search_term='Dies')
for album in albums:
    print('Added:', album.title)
    device.add_to_queue(album)

# Dial up the volume (just a bit) and play
device.volume += 20
device.play()