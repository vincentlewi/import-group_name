import { useState, useEffect } from 'react';
import { motion, useAnimation } from 'framer-motion';
import './StarRating.css';

const starVariants = {
    initial: {
      scale: 0
    },
    animate: i => ({
      scale: 1,
      transition: {
        delay: i * .04,
        duration: .25,
        type: 'spring',
        stiffness: 175
      }
    }),
    exit: i => ({
      scale: 0,
      transition: {
        duration: .25,
        delay: .2 - i * .04,
      }
    }),
    hovered: {
      scale: .8,
      transition: {
        duration: .2
      }
    }
  }
  const Star = ({ i, isHoveringWrapper, isClicked }) => {
    const [isHovering, setIsHovering] = useState(false);
    const starControls = useAnimation();
    const backgroundControls = useAnimation();
    useEffect(() => {
      if (isClicked && isHovering) starControls.start('hovered');
      else if (isClicked) starControls.start('animate');
      else starControls.start('exit');
    }, [isClicked, isHovering]);
    useEffect(() => {
      if (isHoveringWrapper) backgroundControls.start({ background: '#ffd700' });
      else backgroundControls.start({ background: '#aaaaaa' });
    }, [isHoveringWrapper]);
    return (
      <>
        <motion.div 
          className="star-background" 
          initial={{ background: '#aaaaaa' }}
          animate={backgroundControls}
        />
        <motion.i 
          className="fa fa-star" 
          onMouseOver={() => setIsHovering(true)}
          onMouseOut={() => setIsHovering(false)}
          variants={starVariants}
          initial="initial"
          animate={starControls}
          custom={i}
        />
      </>
    )
  }

  function StarRating (props: any) {
    const [clicked, setClicked] = useState(0)
    const [Hovering, setHovering] = useState(0)
    
    useEffect(() => {
      setClicked(props.rating)
      setHovering(props.rating)
    }, [props.rating])

    return (
      <div className="star-rating" onMouseLeave={() => setHovering(0)}>
        <div className="stars-container">
          {[1, 2, 3, 4, 5].map((i) => (
            <motion.div 
              className="star-wrapper"
              onMouseOver={() => setHovering(i)}
              onClick={() => {i!=clicked ? (setClicked(i), props.setRating(i)) : (setClicked(0), props.setRating(0))}}
              key={i}
            >
              <Star 
                i={i} 
                isHoveringWrapper={Hovering >= i} 
                isClicked={clicked >= i}    
              />
            </motion.div>
          ))}
        </div>
      </div>
    )
  }

export default StarRating;