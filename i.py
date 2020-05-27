#import tensorflow as tf
import tensorflow.compat.v1 as tf

hello = tf.constant('Hello, TensorFlow!')
sess = tf.Session()

print(sess.run(hello))