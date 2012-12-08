from setuptools import setup, find_packages

setup(name="django-paypal-subscription",
           version="0.1",
           description="Subscriptions based web app using django-paypal. Based off original work by SAAS-Kit's Django-subscription",
           author="Mart van de Ven",
           author_email="m@type.hk",
           packages=find_packages(),
           include_package_data=True,
)

