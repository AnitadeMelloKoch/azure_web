import tensorflow as tf
import numpy as np
from sklearn.metrics import roc_auc_score, accuracy_score
import argparse

# import get_data as get

def predict(data, meta_dir, checkpoint_dir, validate):
    
    x =  tf.compat.v1.placeholder("float", [None, 225], name="x")

    with tf.Session() as sess:
        # initialize saver and load graph
        saver = tf.compat.v1.train.import_meta_graph(meta_dir)
        saver.restore(sess, tf.train.latest_checkpoint(checkpoint_dir))
        graph = tf.compat.v1.get_default_graph()

        # load all weights and biases from previous graph
        weight_1 = graph.get_tensor_by_name("weight_1:0")
        bias_1 = graph.get_tensor_by_name("weight_1_bias:0")
        weight_2 = graph.get_tensor_by_name("weight_2:0")
        bias_2 = graph.get_tensor_by_name("weight_2_bias:0")
        weight_3 = graph.get_tensor_by_name("weight_3:0")
        bias_3 = graph.get_tensor_by_name("weight_3_bias:0")
        weight_4 = graph.get_tensor_by_name("weight_4:0")
        bias_4 = graph.get_tensor_by_name("weight_4_bias:0")
        weight_5 = graph.get_tensor_by_name("weight_5:0")
        bias_5 = graph.get_tensor_by_name("weight_5_bias:0")
        weight_6 = graph.get_tensor_by_name("weight_6:0")
        bias_6 = graph.get_tensor_by_name("weight_6_bias:0")
        weight_action_1_layer_1 = graph.get_tensor_by_name("weight_action_1_layer_1:0")
        bias_action_1_layer_1 = graph.get_tensor_by_name("weight_action_1_layer_1_bias:0")
        weight_action_2_layer_1 = graph.get_tensor_by_name("weight_action_2_layer_1:0")
        bias_action_2_layer_1 = graph.get_tensor_by_name("weight_action_2_layer_1_bias:0")
        weight_out_action_1 = graph.get_tensor_by_name("weight_out_action_1:0")
        bias_out_action_1 = graph.get_tensor_by_name("weight_out_action_1_bias:0")
        weight_out_action_2 = graph.get_tensor_by_name("weight_out_action_2:0")
        bias_out_action_2 = graph.get_tensor_by_name("weight_out_action_2_bias:0")
        weight_out_loc = graph.get_tensor_by_name("weight_out_loc:0")
        bias_out_loc = graph.get_tensor_by_name("weight_out_loc_bias:0")
        weight_out_phone = graph.get_tensor_by_name("weight_out_phone:0")
        bias_out_phone = graph.get_tensor_by_name("weight_out_phone_bias:0")
        
        # initialize all layers
        layer_1 = tf.nn.sigmoid(tf.add(tf.matmul(x, weight_1), bias_1))
        layer_2 = tf.nn.sigmoid(tf.add(tf.matmul(layer_1, weight_2), bias_2))
        layer_3 = tf.nn.sigmoid(tf.add(tf.matmul(layer_2, weight_3), bias_3))
        layer_4 = tf.nn.sigmoid(tf.add(tf.matmul(layer_3, weight_4), bias_4))
        layer_5 = tf.nn.sigmoid(tf.add(tf.matmul(layer_4, weight_5), bias_5))
        layer_6 = tf.nn.sigmoid(tf.add(tf.matmul(layer_5, weight_6), bias_6))
        layer_action_1_layer_1 = tf.nn.sigmoid(tf.add(tf.matmul(layer_6, weight_action_1_layer_1), bias_action_1_layer_1))
        layer_action_2_layer_1 = tf.nn.sigmoid(tf.add(tf.matmul(layer_6, weight_action_2_layer_1), bias_action_2_layer_1))

        # initialize predictions
        predicted_action_1 = tf.sigmoid(tf.add(tf.matmul(layer_action_1_layer_1, weight_out_action_1), bias_out_action_1))
        predicted_action_2 = tf.sigmoid(tf.add(tf.matmul(layer_action_2_layer_1, weight_out_action_2), bias_out_action_2))
        predicted_loc = tf.sigmoid(tf.add(tf.matmul(layer_6, weight_out_loc), bias_out_loc))
        predicted_phone = tf.sigmoid(tf.add(tf.matmul(layer_6, weight_out_phone), bias_out_phone))

        data_in = np.asarray(data)

        print("Starting prediction")
        action_1 = sess.run(predicted_action_1, feed_dict={x:data_in})
        action_2 = sess.run(predicted_action_2, feed_dict={x:data_in})
        loc = sess.run(predicted_loc, feed_dict={x:data_in})
        phone = sess.run(predicted_phone, feed_dict={x:data_in})
        print(action_1)
        print(action_2)
        print(loc)
        print(phone)

        output = np.concatenate((action_1, action_2, loc, phone), axis=1)

        return output







if __name__ == '__main__':
    AP = argparse.ArgumentParser()
    AP.add_argument("--data", type=list, help="input data")
    AP.add_argument("--meta_directory", type=str, help="Full path to meta file of model")
    AP.add_argument("--checkpoint_directory", type=str, help="Full path to checkpoint file for model")
    AP.add_argument("--validate", type=bool, default=False, help="Do validation on the dataset. This requires a known output")

    parsed = AP.parse_args()

    predict(data=parsed.data,
            meta_dir=parsed.meta_directory,
            checkpoint_dir=parsed.checkpoint_directory,
            validate=parsed.validate)