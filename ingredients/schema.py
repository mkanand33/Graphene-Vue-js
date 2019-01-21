# cookbook/ingredients/schema.py
import graphene

from graphene_django.types import DjangoObjectType
from graphql_jwt.shortcuts import get_token

from ingredients.models import Category, Ingredient, Product, Family, Location, Link, Blog, Name, Signup, Login, \
    Comment, Rating, Like, Reply
from django.contrib.auth import get_user_model
from django.db.models import Q


class UserType(DjangoObjectType):
    class Meta:
        model = get_user_model()


class CommentType(DjangoObjectType):
    class Meta:
        model = Comment


class ReplyType(DjangoObjectType):
    class Meta:
        model = Reply


class LikeType(DjangoObjectType):
    class Meta:
        model = Like


class RatingType(DjangoObjectType):
    class Meta:
        model = Rating


class SignupType(DjangoObjectType):
    class Meta:
        model = Signup


class LoginType(DjangoObjectType):
    class Meta:
        model = Login


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category


class IngredientType(DjangoObjectType):
    class Meta:
        model = Ingredient


class FamilyType(DjangoObjectType):
    class Meta:
        model = Family


class LocationType(DjangoObjectType):
    class Meta:
        model = Location


class ProductType(DjangoObjectType):
    class Meta:
        model = Product


class LinkType(DjangoObjectType):
    class Meta:
        model = Link


class BlogType(DjangoObjectType):
    class Meta:
        model = Blog


class CreateLink(graphene.Mutation):
    id = graphene.Int()
    url = graphene.String()
    description = graphene.String()

    # 2
    class Arguments:
        url = graphene.String()
        description = graphene.String()

    # 3
    def mutate(self, info, url, description):
        link = Link(url=url, description=description)
        link.save()

        return CreateLink(
            id=link.id,
            url=link.url,
            description=link.description,
        )


class CreateCategory(graphene.Mutation):
    id = graphene.Int()
    name = graphene.String()

    class Arguments:
        name = graphene.String()

    def mutate(self, info, name):
        category = Category(name=name)
        category.save()

        return CreateCategory(
            id=category.id,
            name=category.name,
        )


class CreateBlog(graphene.Mutation):
    id = graphene.Int()
    title = graphene.String()
    content = graphene.String()
    user = graphene.Int()

    class Arguments:
        title = graphene.String()
        content = graphene.String()
        user = graphene.Int()

    def mutate(self, info, title, content, user):
        user_data = get_user_model().objects.get(pk=user)
        blog = Blog(title=title, content=content, user=user_data)
        blog.save()

        return CreateBlog(
            id=blog.id,
            title=blog.title,
            content=blog.content,
            user=blog.user,
        )


class EditBlog(graphene.Mutation):
    id = graphene.Int()
    title = graphene.String()
    content = graphene.String()
    user = graphene.Int()

    class Arguments:
        title = graphene.String()
        content = graphene.String()
        user = graphene.Int()

    def mutate(self, info, title, content, user):
        edit = Blog.objects.get(pk=user)
        edit.title = title
        edit.content = content
        edit.unpublish()
        edit.disapprove()
        edit.save()

        return EditBlog(
            id=edit.id,
            title=edit.title,
            content=edit.content,
            user=edit.user,
        )


class CreateComment(graphene.Mutation):
    id = graphene.Int()
    comment = graphene.String()
    blog = graphene.Int()
    user = graphene.Int()

    class Arguments:
        comment = graphene.String()
        blog = graphene.Int()
        user = graphene.Int()

    def mutate(self, info, comment, blog, user):
        user_data = get_user_model().objects.get(pk=user)
        blog_data = Blog.objects.get(pk=blog)
        message = Comment(comment=comment, blog=blog_data, user=user_data)
        message.save()

        return CreateComment(
            id=message.id,
            comment=message.comment,
            blog=message.blog,
            user=message.user,
        )


class CreateReply(graphene.Mutation):
    id = graphene.Int()
    reply = graphene.String()
    comment = graphene.Int()
    blog = graphene.Int()
    user = graphene.Int()

    class Arguments:
        reply = graphene.String()
        comment = graphene.Int()
        blog = graphene.Int()
        user = graphene.Int()

    def mutate(self, info, reply,comment, blog, user):
        comment_data = Comment.objects.get(pk=comment)
        user_data = get_user_model().objects.get(pk=user)
        blog_data = Blog.objects.get(pk=blog)
        message = Reply(reply=reply, comment=comment_data, blog=blog_data, user=user_data)
        message.save()

        return CreateReply(
            id=message.id,
            reply=message.reply,
            comment=message.comment,
            blog=message.blog,
            user=message.user,
        )


class CreateRating(graphene.Mutation):
    id = graphene.Int()
    rating = graphene.Int()
    blog = graphene.Int()
    user = graphene.Int()

    class Arguments:
        rating = graphene.Int()
        blog = graphene.Int()
        user = graphene.Int()

    def mutate(self, info, rating, blog, user):
        user_data = get_user_model().objects.get(pk=user)
        blog_data = Blog.objects.get(pk=blog)
        message = Rating(rating=rating, blog=blog_data, user=user_data)
        message.save()

        return CreateRating(
            id=message.id,
            rating=message.rating,
            blog=message.blog,
            user=message.user,
        )


class LikeValue(graphene.Mutation):
    id = graphene.Int()
    like = graphene.Int()
    blog = graphene.Int()
    user = graphene.Int()

    class Arguments:
        like = graphene.Int()
        blog = graphene.Int()
        user = graphene.Int()

    def mutate(self, info, like, blog, user):
        user_data = get_user_model().objects.get(pk=user)
        blog_data = Blog.objects.get(pk=blog)
        value = Like(like=like, blog=blog_data, user=user_data)
        value.save()

        return LikeValue(
            id=value.id,
            like=value.like,
            blog=value.blog,
            user=value.user,
        )


class DislikeValue(graphene.Mutation):
    id = graphene.Int()
    dislike = graphene.Int()
    blog = graphene.Int()
    user = graphene.Int()

    class Arguments:
        dislike = graphene.Int()
        blog = graphene.Int()
        user = graphene.Int()

    def mutate(self, info, dislike, blog, user):
        user_data = get_user_model().objects.get(pk=user)
        blog_data = Blog.objects.get(pk=blog)
        value = Like(dislike=dislike, blog=blog_data, user=user_data)
        value.save()

        return LikeValue(
            id=value.id,
            dislike=value.dislike,
            blog=value.blog,
            user=value.user,
        )


class CreateValue(graphene.Mutation):
    id = graphene.Int()
    name = graphene.String()

    class Arguments:
        id = graphene.Int()
        name = graphene.String()

    def mutate(self, info, id, name):
        name = Name(name=name)
        x = Blog.objects.get(id=id)
        x.publish()
        x.approve()

        return CreateValue(
            id=name.id,
            name=name.name
        )


class UnCreateValue(graphene.Mutation):
    id = graphene.Int()
    name = graphene.String()

    class Arguments:
        id = graphene.Int()
        name = graphene.String()

    def mutate(self, info, id, name):
        name = Name(name=name)
        x = Blog.objects.get(id=id)
        x.unpublish()
        x.disapprove()

        return UnCreateValue(
            id=name.id,
            name=name.name
        )


class CreateSignup(graphene.Mutation):
    id = graphene.Int()
    firstname = graphene.String()
    lastname = graphene.String()
    username = graphene.String()
    email = graphene.String()
    password = graphene.String()

    class Arguments:
        firstname = graphene.String()
        lastname = graphene.String()
        username = graphene.String()
        email = graphene.String()
        password = graphene.String()

    def mutate(self, info, firstname, lastname, username, email, password):
        signup = Signup(firstname=firstname, lastname=lastname, username=username, email=email, password=password)
        signup.save()

        return CreateSignup(
            id=signup.id,
            firstname=signup.firstname,
            lastname=signup.lastname,
            username=signup.username,
            email=signup.email,
            password=signup.password,
        )


class CreateLogin(graphene.Mutation):
    user = graphene.Field(SignupType)
    token = graphene.String()

    class Arguments:
        username = graphene.String()
        password = graphene.String()

    def mutate(self, info, password, username):
        token = ''

        # Return token
        if Signup.objects.filter(username=username).exists():
            user = Signup.objects.get(username=username)
            token = get_token(user)
        return CreateLogin(user=user, token=token)


class CreateUser(graphene.Mutation):
    id = graphene.Int()
    firstname = graphene.String()
    lastname = graphene.String()
    username = graphene.String()
    email = graphene.String()
    password = graphene.String()

    class Arguments:
        firstname = graphene.String()
        lastname = graphene.String()
        username = graphene.String(required=True)
        password = graphene.String(required=True)
        email = graphene.String(required=True)

    def mutate(self, info, firstname, lastname, username, password, email):
        user = get_user_model()(
            first_name=firstname,
            last_name=lastname,
            username=username,
            email=email,
        )
        user.set_password(password)
        user.save()

        return CreateUser(
            id=user.id,
            firstname=user.first_name,
            lastname=user.last_name,
            username=user.username,
            email=user.email,
            password=user.password,
        )


class CreateIngredient(graphene.Mutation):
    id = graphene.Int()
    title = graphene.String()
    content = graphene.String()

    class Arguments:
        title = graphene.String()
        content = graphene.String()

    def mutate(self, info, title, content):
        blog = Blog(title=title, content=content)
        blog.save()

        return CreateIngredient(
            id=blog.id,
            title=blog.title,
            content=blog.content,
        )


class Mutation(graphene.ObjectType):
    create_link = CreateLink.Field()
    create_category = CreateCategory.Field()
    create_blog = CreateBlog.Field()
    edit_blog = EditBlog.Field()
    create_value = CreateValue.Field()
    un_create_value = UnCreateValue.Field()
    create_signup = CreateSignup.Field()
    create_login = CreateLogin.Field()
    create_user = CreateUser.Field()
    create_ingredient = CreateIngredient.Field()
    create_comment = CreateComment.Field()
    create_reply = CreateReply.Field()
    create_rating = CreateRating.Field()
    like_value = LikeValue.Field()
    dislike_value = DislikeValue.Field()


#
# class CreateUser(graphene.Mutation):
#     class Arguments:
#         name = graphene.String()
#
#     user = graphene.Field(Category)
#
#     def mutate(self, info, name):
#         user = Category(name=name)
#         return CreateUser(user=user)


# class Mutation(graphene.ObjectType):
#     create_user = CreateUser.Field()


class Query(object):
    all_categories = graphene.List(CategoryType)

    all_ingredients = graphene.List(IngredientType)

    all_families = graphene.List(FamilyType)

    all_locations = graphene.List(LocationType)

    all_products = graphene.List(ProductType)

    all_links = graphene.List(LinkType)

    all_blogs = graphene.List(BlogType)

    all_signups = graphene.List(SignupType)

    all_logins = graphene.List(LoginType)

    all_comments = graphene.List(CommentType)

    all_replies = graphene.List(ReplyType)

    all_ratings = graphene.List(RatingType)

    me = graphene.Field(UserType)

    users = graphene.List(UserType)

    comments = graphene.List(CommentType, search=graphene.Int())

    dates = graphene.List(BlogType, search=graphene.String())

    approve = graphene.List(BlogType, search=graphene.Int())

    rate = graphene.List(RatingType, search=graphene.Int())

    user_check = graphene.Field(UserType,
                                id=graphene.Int(),
                                username=graphene.String())

    category = graphene.Field(CategoryType,
                              id=graphene.Int(),
                              name=graphene.String())

    ingredient = graphene.Field(IngredientType,
                                id=graphene.Int(),
                                name=graphene.String())

    family = graphene.Field(FamilyType,
                            id=graphene.Int(),
                            reference=graphene.String())

    location = graphene.Field(LocationType,
                              id=graphene.Int(),
                              reference=graphene.String())

    product = graphene.Field(ProductType,
                             id=graphene.Int(),
                             sku=graphene.String())

    blog = graphene.Field(BlogType,
                          id=graphene.Int(),
                          user=graphene.Int()
                          )

    def resolve_all_signups(self, info, **kwargs):
        return Signup.objects.all()

    def resolve_all_comments(self, info, **kwargs):
        return Comment.objects.all()

    def resolve_all_replies(self, info, **kwargs):
        return Reply.objects.all()

    def resolve_all_categories(self, info, **kwargs):
        return Category.objects.all()

    def resolve_all_ingredients(self, info, **kwargs):
        # We can easily optimize query count in the resolve method
        return Ingredient.objects.select_related('category').all()

    def resolve_all_families(self, info, **kwargs):
        return Family.objects.all()

    def resolve_all_locations(self, info, **kwargs):
        return Location.objects.all()

    def resolve_all_products(self, info, **kwargs):
        return Product.objects.all()

    def resolve_users(self, info):
        return get_user_model().objects.all()

    def resolve_me(self, info):
        user = info.context.user
        if user.is_anonymous:
            raise Exception('Not logged in!')

        return user

    def resolve_user_check(self, info, **kwargs):
        id = kwargs.get('id')
        username = kwargs.get('username')

        if id is not None:
            return get_user_model().objects.get(pk=id)
        if username is not None:
            return get_user_model().objects.get(username=username)

    def resolve_category(self, info, **kwargs):
        id = kwargs.get('id')
        name = kwargs.get('name')

        if id is not None:
            return Category.objects.get(pk=id)
        if name is not None:
            return Category.objects.get(name=name)
        return None

    def resolve_ingredient(self, info, **kwargs):
        id = kwargs.get('id')
        name = kwargs.get('name')

        if id is not None:
            return Ingredient.objects.get(pk=id)

        if name is not None:
            return Ingredient.objects.get(name=name)

        return None

    def resolve_family(self, info, **kwargs):
        id = kwargs.get('id')
        reference = kwargs.get('reference')

        if id is not None:
            return Family.objects.get(pk=id)

        if reference is not None:
            return Family.objects.get(name=reference)

        return None

    def resolve_location(self, info, **kwargs):
        id = kwargs.get('id')
        reference = kwargs.get('reference')

        if id is not None:
            return Location.objects.get(pk=id)

        if reference is not None:
            return Location.objects.get(name=reference)

        return None

    def resolve_product(self, info, **kwargs):
        id = kwargs.get('id')
        sku = kwargs.get('sku')

        if id is not None:
            return Product.objects.get(pk=id)

        if sku is not None:
            return Product.objects.get(name=sku)

        return None

    def resolve_blog(self, info, **kwargs):
        id = kwargs.get('id')
        user = kwargs.get('user')

        if id is not None:
            return Blog.objects.get(pk=id)

        if user is not None:
            return Blog.objects.get(user_id=user)

        return None

    def resolve_comments(self, info, search=None, **kwargs):
        if search:
            filter = (
                Q(blog__id__icontains=search)
            )
            return Comment.objects.filter(filter)

        return Comment.objects.all()

    def resolve_rate(self,info,search=None,**kwargs):
        if search:
            filter = (
                Q(rating__icontains=search)
            )
            return Rating.objects.filter(filter)
        return Rating.objects.all()

    def resolve_dates(self, info, search=None, **kwargs):
        if search:
            filter = (
                Q(created_date__icontains=search)
            )
            return Blog.objects.filter(filter)

        return Blog.objects.all()

    def resolve_approve(self, info, search=None, **kwargs):
        if search:
            filter = (
                Q(approval__icontains=search)
            )
            return Blog.objects.filter(filter)

        return Blog.objects.all()


    def resolve_all_links(self, info, **kwargs):
        return Link.objects.all()

    def resolve_all_blogs(self, info, **kwargs):
        return Blog.objects.all()

    def resolve_all_logins(self, info, **kwargs):
        return Login.objects.all()
