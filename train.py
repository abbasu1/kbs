import os
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from tensorflow.keras.callbacks import ModelCheckpoint

def build_model():
    """Build a simple CNN model for pneumonia and lung opacity classification."""
    model = Sequential([
        Conv2D(32, (3, 3), activation='relu', input_shape=(224, 224, 3)),
        MaxPooling2D((2, 2)),
        
        Conv2D(64, (3, 3), activation='relu'),
        MaxPooling2D((2, 2)),
        
        Conv2D(128, (3, 3), activation='relu'),
        MaxPooling2D((2, 2)),
        
        Flatten(),
        Dense(128, activation='relu'),
        Dropout(0.5),
        Dense(3, activation='softmax')  # 3-class classification
    ])
    
    model.compile(optimizer='adam',
                  loss='categorical_crossentropy',
                  metrics=['accuracy'])
    return model

def main():
    train_dir = 'dataset/train'
    test_dir = 'dataset/test'
    
    if not os.path.exists(train_dir) or not os.listdir(train_dir):
        print("Dataset not found! Please run prepare_data.py first.")
        return

    # Data augmentation and preprocessing for training
    train_datagen = ImageDataGenerator(
        rescale=1./255,
        rotation_range=20,
        zoom_range=0.2,
        horizontal_flip=True,
        validation_split=0.1  # Use 10% of training data for validation during epoch
    )
    
    # Preprocessing for testing
    test_datagen = ImageDataGenerator(rescale=1./255)
    
    train_generator = train_datagen.flow_from_directory(
        train_dir,
        target_size=(224, 224),
        batch_size=32,
        class_mode='categorical'
    )
    
    test_generator = test_datagen.flow_from_directory(
        test_dir,
        target_size=(224, 224),
        batch_size=32,
        class_mode='categorical'
    )
    
    model = build_model()
    model.summary()
    
    # Save the best model automatically
    checkpoint = ModelCheckpoint('pneumonia_model.h5', monitor='val_accuracy', save_best_only=True, mode='max')
    
    print("Starting training...")
    history = model.fit(
        train_generator,
        epochs=2,
        validation_data=test_generator,
        callbacks=[checkpoint]
    )
    
    # Ensure it's saved even if not the absolute best per checkpoint logic
    model.save('pneumonia_model.h5')
    print("Training complete! Model saved as 'pneumonia_model.h5'")

if __name__ == "__main__":
    main()
