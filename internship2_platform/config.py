class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@localhost/internship2_platform'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'your-secret-key'
    JWT_SECRET_KEY = 'your-jwt-secret-key'