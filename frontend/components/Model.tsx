"use client";
import { useThree } from "@react-three/fiber";
import { useAnimations, useGLTF } from "@react-three/drei";
import { useRef, useEffect } from "react";
import { Group, Box3, Vector3 } from "three";
import useShipModelStore from "@/store/ShipModelStore";

export default function Model() {
	const selectedShipModel = useShipModelStore(
		(state) => state.selectedShipModel
	);
	const ShipModelPath = `/models/ship1/scene.gltf`;
	useGLTF.preload(ShipModelPath);
	const group = useRef<Group>(null);
	const { scene, animations } = useGLTF(ShipModelPath,true);
	const { actions } = useAnimations(animations, scene);
	const { camera } = useThree();
	const { gl } = useThree();
	console.log("actions", actions);
	useEffect(() => {
		if (group.current) {
			// group.current.position.set(1, 0, 5);
			const boundingBox = new Box3().setFromObject(group.current);
			const center = boundingBox.getCenter(new Vector3());
			const size = boundingBox.getSize(new Vector3()).length();
			gl.setClearColor("#FFFFFF1A",0);
			// Adjust the camera to fit the model
			// camera.position.set(center.x, center.y, size + 8 );
			camera.position.set(center.x + size * 2, center.y, center.z);
			camera.lookAt(center);
			camera.zoom = 3.0; // Set the zoom level (increase for zoom-in, decrease for zoom-out)
			camera.updateProjectionMatrix();
		}
	}, [group, camera, gl]);

	return (
		<group ref={group}>
			<primitive object={scene} />
		</group>
	);
}
