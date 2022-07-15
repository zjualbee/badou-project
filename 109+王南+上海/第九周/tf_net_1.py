import matplotlib.pyplot as plt
import tensorflow as tf
import numpy as np

input_number = 50
node_number = 10
out_number = input_number

x = np.linspace(-1, 1, input_number).reshape(-1, 1)
print(x.shape)
noise = np.random.normal(0, 0.05, x.shape)
y = x**2 + noise
print(y.shape)

input_x = tf.compat.v1.placeholder(tf.float32, [input_number, 1])
input_y = tf.compat.v1.placeholder(tf.float32, [input_number, 1])

l1_w = tf.Variable(tf.random.normal((node_number, input_number)))
l1_bias = tf.Variable(tf.zeros((1, 1), dtype=tf.float32), dtype=tf.float32)
l1_in = tf.matmul(l1_w, input_x) + l1_bias
l1_out = tf.nn.tanh(l1_in)

l2_w = tf.Variable(tf.random.normal((out_number, node_number)))
l2_bias = tf.Variable(tf.zeros((1, 1), dtype=tf.float32), dtype=tf.float32)
l2_in = tf.matmul(l2_w, l1_out) + l2_bias
l2_out = tf.nn.tanh(l2_in)

loss = tf.reduce_mean(tf.square(l2_out - input_y))
train = tf.train.GradientDescentOptimizer(0.1).minimize(loss)

with tf.Session() as session:
    session.run(tf.global_variables_initializer())
    for i in range(50000):
        session.run(train, feed_dict={input_x:x, input_y:y})

    predictions = session.run(l2_out, feed_dict={input_x:x})

    print(x.shape)

    print(predictions.shape)

    plt.figure()
    plt.scatter(x, y)
    plt.scatter(x, predictions, marker="*", edgecolors="r")
    plt.show()

