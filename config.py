
VOCAB_THRESHOLD = 10


BUCKETS = [(10, 15), (15, 25), (25, 45), (45, 60), (60, 100)] #First try buckets you can tweak these

EPOCHS = 100

BATCH_SIZE = 64

RNN_SIZE = 512

NUM_LAYERS = 3

ENCODING_EMBED_SIZE = 512
DECODING_EMBED_SIZE = 512

LEARNING_RATE = 0.0001
LEARNING_RATE_DECAY = 0.9 #nisam siguran da cu ovo koristiti
MIN_LEARNING_RATE = 0.0001

KEEP_PROBS = 0.5

CLIP_RATE = 4