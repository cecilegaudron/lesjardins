from django.test import TestCase

# Create your tests here.
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>My Wish List</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css">

    <style>
        .light-red {
            background-color: #FFDDDD;
        }
        .light-green {
            background-color: #CCFFCC;
        }
        body {
          background: linear-gradient(180deg, #ebf4f5, #b5c6e0);
          background-size: 100% 100%;
          background-repeat: no-repeat;
          background-attachment: fixed;
          background-position: center;
          background-size: cover;
      }
    </style>
</head>
<body>
    <div class="container">
        <div class="row">
            <div class="col-md-8 mx-auto">
              <br>
                <h1 class="text-center mb-5">My Wish List</h1>
            </div>
        </div>

        <div class="row mb-3">
            <div class="col-md-12 mx-auto">
                <a href="{% url 'CreateWish' %}" class="btn btn-primary">Add New</a>
            </div>
        </div>


        <div class="row">
            {% for wish in wishes %}
                <div class="col-md-4 mb-4">
                    <div class="card {% if wish.is_achieved %}light-green{% else %}light-red{% endif %}">
                        <img src="{{ wish.image.url }}" class="card-img-top" alt="{{ wish.wishtitle }}">
                        <div class="card-body">
                            <h5 class="card-title">{{ wish.wishtitle }}</h5>
                            <p class="card-text">{{ wish.wish }}</p>
                            <a href="{{ wish.link }}" class="btn btn-primary" target="_blank">Buy Now</a>
                            <a href="{% url 'UpdateWish' wish.id %}" class="btn btn-secondary">Edit</a>
                            <a href="{% url 'DeleteWish' wish.id %}" class="btn btn-danger">Delete</a>
                        </div>
                        <div class="card-footer text-muted">
                            Created: {{ wish.date }}
                        </div>
                    </div>
                </div>
            {% endfor %}
        </div>
    </div>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>