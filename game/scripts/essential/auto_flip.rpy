init -1 python:
    from renpy.curry import curry
    
    def check_flip_direction_with_tag(tag, trans, st, at):
        try:
            attributes = renpy.get_attributes(tag)
            
            if attributes and 'left' in attributes:
                trans.xzoom = -1.0 
            else:
                trans.xzoom = 1.0
        except Exception as e:
            renpy.log(f"Error in auto_flip for {tag}: {e}")
            trans.xzoom = 1.0
        return None

    curried_flip = curry(check_flip_direction_with_tag)

init -1:
    transform auto_flip(tag):
        function curried_flip(tag)