64, (3,3), activation='relu', padding='same'))
            model.add(keras.layers.Conv2D(64, (3,3), activation='relu', padding='same'))
                        model.add(keras.layers.MaxPooling2D(2,2))

                                    # The third convolution
                                                model.add(keras.layers.Conv2D(128, (3,3), activation='relu', padding='same'))
                                                            model.add(keras.layers.Conv2D(128, (3,3), activation='relu', padding='same'))
                                                                        model.add(keras.layers.MaxPooling2D(2,2))
                                                                                    model.add(keras.layers.Flatten())
else:
                model.add(keras.layers.Flatten(input_shape=INPUT_SHAPE))

                        hp_units = hp.Int('units', min_value=32, max_value=512, step=32)
                                model.add(keras.layers.Dense(units=hp_units, activation='relu',kernel_regularizer=tf.keras.regularizers.L1(l1=self.L1)))
                                        model.add(keras.layers.Dense(10, activation='softmax'))

                                                hp_learning_rate = hp.Choice('learning_rate', values=[1e-2, 1e-3, 1e-4])
                                                        model.compile(optimizer=keras.optimizers.Adam(learning_rate=hp_learning_rate),
                                                                                        loss='categorical_crossentropy',
                                                                                        metrics=['accuracy'])
                                                                model.summary()
                                                                        return model~
